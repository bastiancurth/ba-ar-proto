# -*- coding: utf-8 -*-
"""Gemeinsame Helfer fuer die Werkzeug-Skripte (ffmpeg/ffprobe, Pfade)."""
import json
import shutil
import subprocess
from pathlib import Path

REPO   = Path(__file__).resolve().parent.parent
ABGABE = REPO / "Abgabe_Masterarbeit_Curth" / "04_Medien"
WERKE  = ["loriot", "bielefeld", "knitter", "roland", "fontane", "wackelauto", "mona"]

def ffmpeg_da():
    return shutil.which("ffmpeg") is not None and shutil.which("ffprobe") is not None

def ffmpeg_hinweis():
    print("ffmpeg fehlt! Einmalig installieren (Eingabeaufforderung):")
    print("  winget install --id Gyan.FFmpeg")
    print("Danach ein neues Fenster oeffnen und das Skript erneut starten.")

def masse(datei):
    """(Breite, Hoehe) eines Videos ODER Bildes per ffprobe, sonst None."""
    try:
        r = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=width,height,avg_frame_rate",
             "-of", "json", str(datei)],
            capture_output=True, text=True, timeout=30)
        st = json.loads(r.stdout)["streams"][0]
        return int(st["width"]), int(st["height"])
    except Exception:
        return None

def platzhalter_weg(zieldatei):
    """Passenden .PLATZHALTER.txt loeschen, sobald die echte Datei da ist."""
    ph = zieldatei.parent / (zieldatei.name + ".PLATZHALTER.txt")
    if ph.is_file():
        try: ph.unlink(); print("   Platzhalter geloescht:", ph.name)
        except OSError: pass
