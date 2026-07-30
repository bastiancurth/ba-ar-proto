# -*- coding: utf-8 -*-
"""Lokaler Testserver MIT Range-Support (python -m http.server kann das nicht;
Browser brauchen Ranges fuer Video-Spruenge). Start ueber LOKAL_STARTEN.bat."""
import os, re
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

class RangeHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Nie cachen: beim lokalen Testen sollen getauschte Videos sofort sichtbar sein
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()
    def send_head(self):
        pfad = self.translate_path(self.path)
        bereich = self.headers.get("Range")
        if not (bereich and os.path.isfile(pfad)):
            return super().send_head()
        m = re.match(r"bytes=(\d*)-(\d*)", bereich)
        if not m:
            return super().send_head()
        groesse = os.path.getsize(pfad)
        start = int(m.group(1)) if m.group(1) else 0
        ende = int(m.group(2)) if m.group(2) else groesse - 1
        ende = min(ende, groesse - 1)
        if start > ende:
            self.send_error(416); return None
        f = open(pfad, "rb"); f.seek(start)
        self.send_response(206)
        self.send_header("Content-Type", self.guess_type(pfad))
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Range", "bytes %d-%d/%d" % (start, ende, groesse))
        self.send_header("Content-Length", str(ende - start + 1))
        self.end_headers()
        self._rest = ende - start + 1
        return f

    def copyfile(self, quelle, ziel):
        rest = getattr(self, "_rest", None)
        if rest is None:
            return super().copyfile(quelle, ziel)
        while rest > 0:
            block = quelle.read(min(65536, rest))
            if not block: break
            ziel.write(block); rest -= len(block)

if __name__ == "__main__":
    print("Lokaler Server (mit Range-Support) auf http://localhost:8000")
    ThreadingHTTPServer(("", 8000), RangeHandler).serve_forever()
