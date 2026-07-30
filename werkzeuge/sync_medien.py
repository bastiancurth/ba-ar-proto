# -*- coding: utf-8 -*-
"""
SYNC: Abgabe-Ordner <-> App-Assets
==================================
Gleicht 04_Medien mit dem assets-Ordner der Web-App ab. Es wird nie etwas
ueberschrieben, nur fehlende Gegenstuecke werden ergaenzt:

  03_Videos_final/<werk>/<werk>.mp4  ->  assets/videos/<werk>.mp4   (komprimiert!)
  04_Audio_final/<werk>/<werk>.mp3   ->  assets/audio/<werk>.mp3
  04_Audio_final/.../<werk>_antwort_N.mp3 -> assets/audio/antworten/
  06_Marker_NFT/<werk>/<werk>.*      ->  assets/markers/<werk>/
  01_Ausgangsbilder/<werk>/<werk>.jpg -> assets/bilder/<werk>.jpg   (Standbild)

  ... und umgekehrt: was nur in assets liegt, wird in den Abgabe-Ordner
  kopiert (so wurde z. B. die fertige Mona Lisa automatisch eingesammelt).

Passende .PLATZHALTER.txt werden dabei geloescht, danach laeuft der
Medien-Check und aktualisiert MEDIEN_STATUS.html.

Start: SYNC_MEDIEN.bat doppelklicken (nach jedem Befuellen).
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path
from hilfen import REPO, ABGABE, WERKE, ffmpeg_da, ffmpeg_hinweis, platzhalter_weg

aktionen = 0

def melde(text):
    global aktionen
    aktionen += 1
    print(" *", text)

def kopiere(quelle, ziel):
    ziel.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(quelle, ziel)
    platzhalter_weg(ziel)
    melde(f"{quelle.relative_to(REPO)}  ->  {ziel.relative_to(REPO)}")

def paar(abgabe_datei, asset_datei, video=False):
    """Fehlende Seite ergaenzen. Videos werden Richtung App komprimiert."""
    a, b = Path(abgabe_datei), Path(asset_datei)
    if a.is_file() and not b.is_file():
        if video and ffmpeg_da():
            from video_komprimieren import komprimieren
            b.parent.mkdir(parents=True, exist_ok=True)
            print(" * komprimiere", a.name, "fuer die App ...")
            if komprimieren(a, b):
                platzhalter_weg(b)
                global aktionen; aktionen += 1
        else:
            if video:
                print("   (Hinweis: ffmpeg fehlt, kopiere unkomprimiert)")
            kopiere(a, b)
    elif b.is_file() and not a.is_file():
        kopiere(b, a)

if __name__ == "__main__":
    if not ffmpeg_da():
        ffmpeg_hinweis()
        print("Sync laeuft trotzdem, Videos werden dann nur kopiert statt komprimiert.\n")

    for w in WERKE:
        paar(ABGABE / "03_Videos_final" / w / (w + ".mp4"), REPO / "assets" / "videos" / (w + ".mp4"), video=True)
        paar(ABGABE / "03_Videos_final" / w / (w + "_idle.mp4"), REPO / "assets" / "videos" / (w + "_idle.mp4"), video=True)
        paar(ABGABE / "04_Audio_final" / w / (w + ".mp3"),  REPO / "assets" / "audio"  / (w + ".mp3"))
        for e in (".iset", ".fset", ".fset3"):
            paar(ABGABE / "06_Marker_NFT" / w / (w + e), REPO / "assets" / "markers" / w / (w + e))
        paar(ABGABE / "01_Ausgangsbilder" / w / (w + ".jpg"), REPO / "assets" / "bilder" / (w + ".jpg"))
        # vertonte Chat-Antworten: egal wo sie in 04_Audio_final liegen
        for mp3 in (ABGABE / "04_Audio_final").rglob(w + "_antwort_*.mp3"):
            ziel = REPO / "assets" / "audio" / "antworten" / mp3.name
            if not ziel.is_file():
                kopiere(mp3, ziel)

    print(f"\nFertig, {aktionen} Datei(en) synchronisiert." if aktionen
          else "\nAlles schon synchron, nichts zu tun.")
    # Status neu erzeugen (oeffnet MEDIEN_STATUS.html im Browser)
    subprocess.run([sys.executable, str(ABGABE / "medien_check.py")])
