# -*- coding: utf-8 -*-
"""
VIDEO KOMPRIMIEREN (ffmpeg, Web-AR-optimiert)
=============================================
Komprimiert Videos so, dass sie im mobilen Browser schnell laden und auf
jedem Geraet abspielen: H.264, max. 1280 px Kante, 30 fps, yuv420p,
faststart (Streaming ab der ersten Sekunde), Ton auf angenehme
Lautstaerke normalisiert (nicht zu laut, Museums-Regel).

Aufruf:
  py video_komprimieren.py DATEI [DATEI2 ...]   einzelne Videos
  py video_komprimieren.py                      alle Videos in 04_Medien/03_Videos_final/
Oder Videos einfach auf VIDEO_KOMPRIMIEREN.bat ziehen (Drag & Drop).

Das Original bleibt unangetastet, Ergebnis: <name>_web.mp4 daneben.
Der Sync (SYNC_MEDIEN.bat) nutzt dieselben Einstellungen automatisch.
"""
import subprocess
import sys
from pathlib import Path
from hilfen import ABGABE, ffmpeg_da, ffmpeg_hinweis, masse

def hat_ton(datei):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a",
                        "-show_entries", "stream=codec_type", "-of", "csv=p=0", str(datei)],
                       capture_output=True, text=True)
    return "audio" in r.stdout

def komprimieren(quelle, ziel):
    quelle, ziel = Path(quelle), Path(ziel)
    ziel.parent.mkdir(parents=True, exist_ok=True)
    filter_v = "scale='min(1280,iw)':-2:flags=lanczos,fps=30"
    befehl = ["ffmpeg", "-y", "-i", str(quelle),
              "-c:v", "libx264", "-preset", "slow", "-crf", "25",
              "-vf", filter_v, "-pix_fmt", "yuv420p", "-movflags", "+faststart"]
    if hat_ton(quelle):
        # Lautheit normalisieren: -18 LUFS ist angenehm leise fuer Innenraeume
        befehl += ["-c:a", "aac", "-b:a", "128k", "-af", "loudnorm=I=-18:TP=-2:LRA=11"]
    else:
        befehl += ["-an"]
    befehl.append(str(ziel))
    r = subprocess.run(befehl, capture_output=True, text=True)
    if r.returncode != 0:
        print("FEHLER bei", quelle.name, "\n", r.stderr[-600:])
        return False
    vorher = quelle.stat().st_size / 1e6
    nachher = ziel.stat().st_size / 1e6
    print(f"OK  {quelle.name}: {vorher:.1f} MB -> {nachher:.1f} MB  ({masse(ziel)[0]}x{masse(ziel)[1]} px)")
    return True

if __name__ == "__main__":
    if not ffmpeg_da():
        ffmpeg_hinweis(); sys.exit(1)
    dateien = [Path(a) for a in sys.argv[1:]]
    if not dateien:
        dateien = [d for d in (ABGABE / "03_Videos_final").rglob("*.mp4")
                   if not d.stem.endswith("_web")]
        print("Keine Datei angegeben, nehme alle Videos aus 03_Videos_final/ ...")
    if not dateien:
        print("Nichts zu tun: keine Videos gefunden.")
    for d in dateien:
        komprimieren(d, d.with_name(d.stem + "_web.mp4"))
