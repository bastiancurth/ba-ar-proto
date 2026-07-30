# -*- coding: utf-8 -*-
"""
ABGABE-SNAPSHOT: Repo-Root -> Abgabe_Masterarbeit_Curth/03_Prototyp_Code
========================================================================
Der Repo-Root ist die EINZIGE Arbeitskopie der Web-App (GitHub Pages liefert
sie live aus). Dieses Skript kopiert den aktuellen Stand als Schnappschuss in
den Abgabe-Ordner, damit die Abgabe in sich geschlossen ist.

Kopiert werden: index.html, index_v2.html, werke.js, WERK_HINZUFUEGEN.txt
und der komplette assets-Ordner. Es wird nur IN die Abgabe kopiert, nie zurueck.

Start: ABGABE_SNAPSHOT.bat doppelklicken (spaetestens einmal vor der Abgabe).
"""
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ZIEL = REPO / "Abgabe_Masterarbeit_Curth" / "03_Prototyp_Code"

n = 0
for name in ("index.html", "index_v2.html", "werke.js", "WERK_HINZUFUEGEN.txt"):
    q = REPO / name
    if q.is_file():
        shutil.copy2(q, ZIEL / name); n += 1

# Redaktions-Werkstatt gehoert in die Abgabe, das private Basti-Cockpit NICHT.
for name in ("werkstatt.py", "WERKSTATT.bat", "marker_erstellen.py", "lokal_server.py", "hilfen.py"):
    q = REPO / "werkzeuge" / name
    if q.is_file():
        (ZIEL / "werkzeuge").mkdir(parents=True, exist_ok=True)
        shutil.copy2(q, ZIEL / "werkzeuge" / name); n += 1

for q in (REPO / "assets").rglob("*"):
    if q.is_file():
        z = ZIEL / "assets" / q.relative_to(REPO / "assets")
        z.parent.mkdir(parents=True, exist_ok=True)
        if (not z.is_file()) or z.stat().st_mtime < q.stat().st_mtime or z.stat().st_size != q.stat().st_size:
            shutil.copy2(q, z); n += 1

print(f"Schnappschuss fertig, {n} Datei(en) kopiert/aktualisiert.")
print("Ziel:", ZIEL)
