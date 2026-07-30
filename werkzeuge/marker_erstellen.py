# -*- coding: utf-8 -*-
"""
NFT-MARKER LOKAL ERSTELLEN (Windows + Mac)
==========================================
Erzeugt die drei Tracking-Dateien (.iset/.fset/.fset3) direkt aus dem
Ausgangsbild, ohne Webseite. Der NFT-Marker-Creator liegt schon unter
werkzeuge/NFT-Marker-Creator/; fehlende Node-Pakete installiert dieses
Skript beim ersten Start automatisch.

Ablauf pro Bild:
  1. Qualitaets-Vorpruefung (Confidence 0-5): sagt vorher, ob das Bild
     als Marker taugt. Faustregeln aus dem offiziellen Guide:
     viel Detail/Kontrast im Bild = gut, hohe Aufloesung = gut.
  2. Erzeugung der drei Dateien, Ablage in App UND Abgabe-Ordner.

WICHTIG (Louvre-Lektion der Masterarbeit): Immer GENAU das Bild
verwenden, das spaeter auch gedruckt wird. Nie ein aehnliches!

Aufruf:
  py marker_erstellen.py loriot      nimmt 01_Ausgangsbilder/loriot/loriot.jpg
  py marker_erstellen.py BILD.jpg    beliebiges Bild (fragt nach dem Werk)
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path
from hilfen import REPO, ABGABE, WERKE, ffmpeg_da, masse, platzhalter_weg

TOOL = Path(__file__).resolve().parent / "NFT-Marker-Creator"

def npm_kommando():
    return shutil.which("npm") or shutil.which("npm.cmd")

def vorbereiten():
    """Node pruefen und Abhaengigkeiten bei Bedarf automatisch installieren."""
    if not (TOOL / "app.js").is_file():
        print("NFT-Marker-Creator fehlt unter werkzeuge/NFT-Marker-Creator/."); return False
    if shutil.which("node") is None:
        print("Node.js fehlt! Einmalig installieren:")
        print("  Windows:  winget install OpenJS.NodeJS.LTS")
        print("  Mac:      brew install node    (oder nodejs.org)")
        return False
    if not (TOOL / "node_modules").is_dir():
        npm = npm_kommando()
        if npm is None:
            print("npm nicht gefunden (kommt normalerweise mit Node.js mit)."); return False
        print("Erster Start: installiere die Node-Pakete des Marker-Creators ...")
        r = subprocess.run([npm, "install", "--no-audit", "--no-fund"], cwd=TOOL)
        if r.returncode != 0:
            print("npm install fehlgeschlagen, Meldung oben pruefen."); return False
    return True

def node_flags():
    """Modernes Node (18+) hat eingebautes fetch, an dem der alte WASM-Lader des
    Tools scheitert ("Failed to parse URL ... .wasm"). Das Flag schaltet es ab;
    aeltere Node-Versionen kennen das Flag nicht und laufen ohne."""
    probe = subprocess.run(["node", "--no-experimental-fetch", "-e", "0"],
                           capture_output=True, text=True)
    return ["--no-experimental-fetch"] if probe.returncode == 0 else []

def laufen_lassen(argumente):
    """app.js erwartet den Bildpfad RELATIV zum Tool-Ordner."""
    return subprocess.run(["node"] + node_flags() + ["app.js"] + argumente, cwd=TOOL,
                          capture_output=True, text=True, input="\n" * 5)

def erstellen(bild, werk):
    if not vorbereiten(): return False
    bild = Path(bild).resolve()
    if ffmpeg_da():
        m = masse(bild)
        if m and min(m) < 800:
            print(f"WARNUNG: Bild nur {m[0]}x{m[1]} px. Der Guide empfiehlt hohe")
            print("Aufloesung, besser mindestens 1000 px kurze Kante verwenden.")
    # Bild in den Tool-Ordner kopieren (app.js kann nur relative Pfade)
    tmp = TOOL / ("_eingabe" + bild.suffix.lower())
    shutil.copy2(bild, tmp)
    try:
        # --- 1. Qualitaets-Vorpruefung ---
        print("Pruefe Marker-Qualitaet von", bild.name, "...")
        r = laufen_lassen(["-onlyConfidence", "-i", tmp.name])
        m = re.search(r"\[([\*\.]*)\]\s*([\d.]+)/5", r.stdout)
        if m:
            wert = float(m.group(2))
            print(f"Confidence: {wert}/5", end="  ")
            if wert >= 4:   print("-> sehr gut, wird zuverlaessig tracken.")
            elif wert >= 3: print("-> brauchbar, im Zweifel vor Ort testen.")
            else:
                print("-> schwach! Tipp aus dem offiziellen Guide: detailreiches,")
                print("   kontrastreiches Bild in hoher Aufloesung verwenden.")
                if input("Trotzdem erzeugen? (j/n) ").strip().lower() != "j":
                    return False
        # --- 2. Marker erzeugen ---
        print("Erzeuge Marker ... (je nach Bild 1-5 Minuten)")
        r = laufen_lassen(["-i", tmp.name, "-NoConf"])
        if r.returncode != 0:
            print("Fehlgeschlagen:\n", (r.stdout + r.stderr)[-600:]); return False
    finally:
        try: tmp.unlink()
        except OSError: pass
    ausgabe = TOOL / "output"
    erzeugt = [d for e in ("*.iset", "*.fset", "*.fset3") for d in ausgabe.glob(e)]
    if not erzeugt:
        print("Keine Ausgabedateien in", ausgabe, "gefunden."); return False
    for ziel_ordner in (REPO / "assets" / "markers" / werk, ABGABE / "06_Marker_NFT" / werk):
        ziel_ordner.mkdir(parents=True, exist_ok=True)
        for d in erzeugt:
            ziel = ziel_ordner / (werk + d.suffix)
            shutil.copy2(d, ziel)
            platzhalter_weg(ziel)
            print("  ->", ziel.relative_to(REPO))
    for d in erzeugt:   # Tool-Ausgabe leeren, sonst landet sie beim naechsten Werk mit drin
        try: d.unlink()
        except OSError: pass
    print("Fertig. werke.js zeigt schon auf assets/markers/%s/%s" % (werk, werk))
    return True

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else input(
        "Welches Werk? (%s) oder Pfad zu einem Bild: " % "/".join(WERKE)).strip()
    if arg in WERKE:
        bild = ABGABE / "01_Ausgangsbilder" / arg / (arg + ".jpg")
        if not bild.is_file():
            print("Ausgangsbild fehlt noch:", bild); sys.exit(1)
        erstellen(bild, arg)
    elif Path(arg).is_file():
        werk = input("Fuer welches Werk? (%s): " % "/".join(WERKE)).strip()
        if werk not in WERKE: print("Unbekanntes Werk."); sys.exit(1)
        erstellen(Path(arg), werk)
    else:
        print("Weder Werk noch Bilddatei gefunden:", arg)
