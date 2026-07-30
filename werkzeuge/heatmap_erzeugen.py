# -*- coding: utf-8 -*-
"""
HEATMAP_ERZEUGEN: Tracking-Merkmalsanalyse fuer Abbildung 4.11
==============================================================
Hintergrund: Der NFT-Marker-Creator liefert nur einen Confidence-WERT
(z. B. 4,47/5 fuer W2), aber keine Bildausgabe der Merkmale. Fuer die
Abbildung wird die Merkmalsverteilung deshalb mit einer Standard-
Eckendetektion nachgerechnet (Shi-Tomasi / cv2.goodFeaturesToTrack auf
zwei Skalen), wie sie natürlichen Bild-Trackern zugrunde liegt, und als
Punktwolke + Dichte-Heatmap visualisiert. Massgeblich fuer die
Produktionsentscheidungen blieb der Confidence-Wert des Tools.

Aufruf:  python heatmap_erzeugen.py [bildpfad]   (Standard: mona.jpg)
Ausgabe: 08_Abbildungen_der_Arbeit/01_Kapitel/abb_marker_heatmap.png
Benoetigt: pip install opencv-python-headless pillow numpy
"""
import sys, os
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BILD = sys.argv[1] if len(sys.argv) > 1 else str(REPO / "assets" / "bilder" / "mona.jpg")

im = cv2.imread(BILD)
grau = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
H, W = grau.shape
punkte = []
for skala in (1.0, 0.5):
    g = cv2.resize(grau, None, fx=skala, fy=skala)
    ecken = cv2.goodFeaturesToTrack(g, maxCorners=260, qualityLevel=0.04,
                                    minDistance=int(9 / skala))
    if ecken is not None:
        for e in ecken.reshape(-1, 2):
            punkte.append((e[0] / skala, e[1] / skala))

heat = np.zeros((H, W), np.float32)
for x, y in punkte:
    cv2.circle(heat, (int(x), int(y)), 10, 1.0, -1)
heat = cv2.GaussianBlur(heat, (0, 0), 14)
heat = np.clip(heat / np.percentile(heat, 99), 0, 1)
farbe = cv2.applyColorMap((heat * 255).astype(np.uint8), cv2.COLORMAP_TURBO)
mix = cv2.addWeighted(im, 0.62, farbe, 0.38, 0)
for x, y in punkte:
    cv2.drawMarker(mix, (int(x), int(y)), (40, 255, 90), cv2.MARKER_CROSS, 7, 1)

def F(sz, art=""):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if art == "b" else "")
    try: return ImageFont.truetype(p, sz)
    except OSError: return ImageFont.truetype("arial.ttf", sz)   # Windows

ziel_h = 640
def skal(a):
    f = ziel_h / a.shape[0]
    return cv2.resize(a, (int(a.shape[1] * f), ziel_h))
L = skal(cv2.cvtColor(im, cv2.COLOR_BGR2RGB)); R = skal(cv2.cvtColor(mix, cv2.COLOR_BGR2RGB))
pad, steg, unten = 36, 30, 104
B = pad * 2 + L.shape[1] + steg + R.shape[1]
out = Image.new("RGB", (B, pad + ziel_h + unten), "white")
out.paste(Image.fromarray(L), (pad, pad))
out.paste(Image.fromarray(R), (pad + L.shape[1] + steg, pad))
d = ImageDraw.Draw(out)
d.rectangle([pad, pad, pad + L.shape[1], pad + ziel_h], outline=(28, 39, 51), width=2)
d.rectangle([pad + L.shape[1] + steg, pad, pad + L.shape[1] + steg + R.shape[1], pad + ziel_h], outline=(28, 39, 51), width=2)
d.text((pad, pad + ziel_h + 12), "Ausgangsbild", font=F(21, "b"), fill=(28, 39, 51))
d.text((pad + L.shape[1] + steg, pad + ziel_h + 12), "%d Tracking-Merkmale (Heatmap)" % len(punkte), font=F(21, "b"), fill=(28, 39, 51))
d.text((pad, pad + ziel_h + 44), "Dichte Merkmalsregionen (warm) geben dem NFT-Tracking Halt,", font=F(17), fill=(92, 111, 125))
d.text((pad, pad + ziel_h + 68), "strukturarme Flaechen (kalt) nicht.", font=F(17), fill=(92, 111, 125))
ziel = REPO / "Abgabe_Masterarbeit_Curth" / "08_Abbildungen_der_Arbeit" / "01_Kapitel" / "abb_marker_heatmap.png"
out.save(str(ziel))
print("gespeichert:", ziel, "| merkmale:", len(punkte))
