# -*- coding: utf-8 -*-
"""
SEITENVERHAELTNIS-CHECK (Marker = Video = Bild?)
================================================
Das AR-Video liegt in der App exakt auf dem gedruckten Bild. Das klappt
nur, wenn Ausgangsbild (= Marker-Grundlage), Video und Standbild dasselbe
Seitenverhaeltnis haben. Dieses Skript vergleicht alle drei pro Werk und
kann das Video notfalls automatisch anpassen (mittiger Beschnitt, keine
Verzerrung) - damit es Museen leichter haben.

  py seitenverhaeltnis_check.py         nur pruefen (Bericht)
  py seitenverhaeltnis_check.py --fix   Videos mit Abweichung > 2 %
                                        beschneiden -> <werk>_angepasst.mp4
                                        (Original bleibt liegen; pruefen,
                                        dann selbst in <werk>.mp4 umbenennen)
Start: SEITENVERHAELTNIS_CHECK.bat (fragt, ob angepasst werden soll).
"""
import subprocess
import sys
from pathlib import Path
from hilfen import REPO, ABGABE, WERKE, ffmpeg_da, ffmpeg_hinweis, masse

TOLERANZ = 0.02   # 2 Prozent Abweichung sind ok (Rundung beim Generieren)

def finde(pfade):
    for p in pfade:
        if p.is_file(): return p
    return None

def pruefe(fix=False):
    probleme = 0
    for w in WERKE:
        bild = finde([ABGABE / "01_Ausgangsbilder" / w / (w + ".jpg"),
                      REPO / "assets" / "bilder" / (w + ".jpg")])
        video = finde([ABGABE / "03_Videos_final" / w / (w + ".mp4"),
                       REPO / "assets" / "videos" / (w + ".mp4")])
        if not bild and not video:
            continue
        print(f"\n{w.upper()}")
        mb = masse(bild) if bild else None
        mv = masse(video) if video else None
        if mb: print(f"  Ausgangsbild {mb[0]}x{mb[1]}  (Verhaeltnis {mb[0]/mb[1]:.3f})  {bild.name}")
        else:  print("  Ausgangsbild fehlt noch")
        if mv: print(f"  Video        {mv[0]}x{mv[1]}  (Verhaeltnis {mv[0]/mv[1]:.3f})  {video.name}")
        else:  print("  Video fehlt noch")
        if not (mb and mv):
            continue
        rb, rv = mb[0] / mb[1], mv[0] / mv[1]
        abweichung = abs(rv - rb) / rb
        if abweichung <= TOLERANZ:
            print(f"  PASST (Abweichung {abweichung*100:.1f} %)")
            continue
        probleme += 1
        print(f"  ACHTUNG: weicht {abweichung*100:.1f} % ab - das Video saesse schief auf dem Bild!")
        if fix:
            ziel = video.with_name(w + "_angepasst.mp4")
            # mittig auf das Bild-Verhaeltnis beschneiden (keine Verzerrung)
            if rv > rb:   crop = f"crop=ih*{rb:.6f}:ih"     # Video zu breit
            else:         crop = f"crop=iw:iw/{rb:.6f}"     # Video zu hoch
            r = subprocess.run(["ffmpeg", "-y", "-i", str(video),
                                "-vf", crop + ",scale=trunc(iw/2)*2:trunc(ih/2)*2",
                                "-c:v", "libx264", "-preset", "slow", "-crf", "25",
                                "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                                "-c:a", "copy", str(ziel)],
                               capture_output=True, text=True)
            if r.returncode == 0:
                print(f"  -> beschnitten gespeichert als {ziel.name} ({masse(ziel)[0]}x{masse(ziel)[1]})")
                print(f"     Bitte ansehen und bei Gefallen in {w}.mp4 umbenennen.")
            else:
                print("  -> ffmpeg-Fehler:", r.stderr[-300:])
    print(f"\n{probleme} Werk(e) mit abweichendem Seitenverhaeltnis." if probleme
          else "\nAlle vorhandenen Paare passen zusammen.")

if __name__ == "__main__":
    if not ffmpeg_da():
        ffmpeg_hinweis(); sys.exit(1)
    pruefe(fix="--fix" in sys.argv)
