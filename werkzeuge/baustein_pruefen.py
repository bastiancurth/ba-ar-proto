# -*- coding: utf-8 -*-
"""
BAUSTEIN-PRUEFER fuer werke.js
==============================
Der Geschichtenerzaehler liefert manchmal typografische Anfuehrungszeichen,
zu wenige Fakten oder kaputte Klammern. Dieses Skript prueft und repariert
einen generierten Baustein, BEVOR er in werke.js landet.

Benutzung:
  1. Den Baustein (nur den Teil von { bis }, ) aus AnythingLLM kopieren
     und in die Datei  baustein.txt  hier im werkzeuge-Ordner einfuegen.
  2. BAUSTEIN_PRUEFEN.bat doppelklicken.
  3. Ergebnis: baustein_sauber.txt (bereinigte Fassung) plus Pruefbericht.
     Erst wenn alles gruen ist, den Inhalt nach werke.js kopieren.
Die inhaltliche Pruefung der Fakten gegen die Quellen bleibt Handarbeit!
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HIER = Path(__file__).resolve().parent
QUELLE = HIER / "baustein.txt"

def pruefen():
    if not QUELLE.is_file():
        print("Bitte zuerst den Baustein in die Datei baustein.txt einfuegen")
        print("(hier im werkzeuge-Ordner, notfalls die Datei neu anlegen).")
        return
    t = QUELLE.read_text(encoding="utf-8")

    # 1. Typografische Zeichen reparieren (kommen aus der Chat-Oberflaeche)
    ersetzungen = {"“": '"', "”": '"', "„": '"', "″": '"',
                   "‘": "'", "’": "'", "–": "-", "—": "-"}
    repariert = 0
    for falsch, richtig in ersetzungen.items():
        repariert += t.count(falsch)
        t = t.replace(falsch, richtig)

    # 2. Grundgeruest checken
    meldungen = []
    if repariert: meldungen.append(f"[ok] {repariert} typografische Zeichen repariert.")
    if not t.strip().startswith("{"): meldungen.append("[!!] Baustein beginnt nicht mit {")
    if not t.strip().rstrip(",").endswith("}"): meldungen.append("[!!] Baustein endet nicht mit } bzw. },")
    m = re.search(r'id:\s*"([a-z0-9_]+)"', t)
    if m:
        wid = m.group(1)
        meldungen.append(f"[ok] id: {wid}")
        if "-" in m.group(0): meldungen.append("[!!] id enthaelt Bindestrich, besser nur Kleinbuchstaben.")
        falsche_pfade = [z for z in re.findall(r'assets/[a-z/]*([a-z0-9_-]+)\.(?:mp4|mp3|jpg)', t) if not z.startswith(wid)]
        if falsche_pfade: meldungen.append(f"[!!] Dateipfade passen nicht zur id: {sorted(set(falsche_pfade))}")
    else:
        meldungen.append("[!!] keine id gefunden (id: \"kurzname\" fehlt).")

    fakten_block = re.search(r'fakten:\s*\[(.*?)\]', t, re.S)
    anzahl = len(re.findall(r'"(?:[^"\\]|\\.)+"', fakten_block.group(1))) if fakten_block else 0
    meldungen.append(f"[{'ok' if anzahl == 6 else '!!'}] {anzahl} von 6 Fakten.")
    dialoge = len(re.findall(r'frage:', t))
    meldungen.append(f"[{'ok' if dialoge >= 4 else '!!'}] {dialoge} Chat-Dialoge (Soll: 5).")
    if re.search(r'\[(?!thoughtful|excited|warm|chuckles|pause)[a-z ]+\]', t.split('geschichte:')[1][:800] if 'geschichte:' in t else ""):
        meldungen.append("[!!] Unbekannte Regieanweisung in der geschichte, bitte entfernen (nur die fuenf bekannten Marken sind erlaubt, im geschichte-Feld am besten gar keine).")

    # 3. Syntax-Test mit Node (falls installiert)
    if shutil.which("node"):
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
            f.write("const W = [" + t.strip().rstrip(",") + "];")
            tmp = f.name
        r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
        meldungen.append("[ok] Syntax-Test bestanden (Node)." if r.returncode == 0
                         else "[!!] Syntax-Fehler:\n" + r.stderr.strip()[:400])
    else:
        meldungen.append("[..] Node nicht gefunden, Syntax-Test uebersprungen.")

    (HIER / "baustein_sauber.txt").write_text(t, encoding="utf-8")
    print("\n".join(meldungen))
    print("\nBereinigte Fassung: baustein_sauber.txt")
    print("Denk an die Handarbeit: jeden Fakt gegen die Quellen pruefen!")

if __name__ == "__main__":
    pruefen()
