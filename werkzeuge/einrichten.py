# -*- coding: utf-8 -*-
"""
EINRICHTUNG: installiert alle Abhaengigkeiten der Werkzeuge automatisch.
Funktioniert unter Windows (winget) und macOS (Homebrew).
Einmal ausfuehren, danach laufen alle anderen Skripte.
"""
import platform
import shutil
import subprocess
import sys
from pathlib import Path

TOOL = Path(__file__).resolve().parent / "NFT-Marker-Creator"
WIN = platform.system() == "Windows"
MAC = platform.system() == "Darwin"

def installiere(name, testbefehl, winget_id, brew_name):
    if shutil.which(testbefehl):
        print(f"[ok] {name} ist da."); return True
    print(f"[..] {name} fehlt, installiere ...")
    if WIN and shutil.which("winget"):
        r = subprocess.run(["winget", "install", "--id", winget_id,
                            "--accept-source-agreements", "--accept-package-agreements"])
    elif MAC and shutil.which("brew"):
        r = subprocess.run(["brew", "install", brew_name])
    else:
        print(f"     Bitte {name} von Hand installieren:")
        print(f"     Windows: winget install --id {winget_id}")
        print(f"     Mac:     brew install {brew_name}   (Homebrew: brew.sh)")
        return False
    if r.returncode == 0:
        print(f"[ok] {name} installiert. WICHTIG: dieses Fenster einmal schliessen")
        print("     und neu oeffnen, damit der Befehl gefunden wird.")
        return True
    print(f"[!!] {name}-Installation fehlgeschlagen, Meldung oben lesen.")
    return False

if __name__ == "__main__":
    print("Pruefe Abhaengigkeiten fuer", platform.system(), "...\n")
    installiere("ffmpeg (Video-Werkzeuge)", "ffmpeg", "Gyan.FFmpeg", "ffmpeg")
    node_da = installiere("Node.js (Marker-Generator)", "node", "OpenJS.NodeJS.LTS", "node")
    if node_da and (TOOL / "app.js").is_file() and not (TOOL / "node_modules").is_dir():
        npm = shutil.which("npm") or shutil.which("npm.cmd")
        if npm:
            print("[..] installiere Node-Pakete des Marker-Creators ...")
            subprocess.run([npm, "install", "--no-audit", "--no-fund"], cwd=TOOL)
            print("[ok] Marker-Creator bereit." if (TOOL / "node_modules").is_dir()
                  else "[!!] npm install bitte spaeter mit MARKER_ERSTELLEN erneut versuchen.")
    print("\nEinrichtung abgeschlossen.")
