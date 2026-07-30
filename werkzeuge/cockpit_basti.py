# -*- coding: utf-8 -*-
"""COCKPIT (Basti-Version, PRIVAT): Produktions-Werkzeuge des Autors.
GEHOERT NICHT IN DIE ABGABE und wird vom abgabe_snapshot bewusst nicht kopiert.
Fuer die Redaktion/Laien ist die separate WERKSTATT gedacht."""
import os, sys, subprocess, threading, webbrowser
from pathlib import Path
import tkinter as tk

REPO = Path(__file__).resolve().parent.parent
ABGABE = REPO / "Abgabe_Masterarbeit_Curth"
HELL = "#f2f7f9"; SW = "#1c2733"; CYAN = "#00BAE5"

class Cockpit(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cockpit (Basti): Produktion und Abgabe")
        self.geometry("960x600"); self.configure(bg=HELL)
        tk.Label(self, text="Cockpit", font=("Segoe UI", 22, "bold"), bg=HELL, fg=SW).pack(anchor="w", padx=18, pady=(14, 0))
        tk.Label(self, text="Deine Produktions-Werkzeuge; die Redaktions-Werkstatt ist das separate Fenster (WERKSTATT.bat).",
                 font=("Segoe UI", 10), bg=HELL, fg="#5c6f7d").pack(anchor="w", padx=18)
        rahmen = tk.Frame(self, bg=HELL); rahmen.pack(fill="both", expand=True, padx=14, pady=10)
        links = tk.Frame(rahmen, bg=HELL); links.pack(side="left", fill="y", padx=(0, 10))
        self.log = tk.Text(rahmen, bg="white", fg=SW, font=("Consolas", 10), relief="flat", wrap="word")
        self.log.pack(side="left", fill="both", expand=True)

        def knopf(text, cmd, primaer=False):
            tk.Button(links, text=text, command=cmd, font=("Segoe UI", 11, "bold" if primaer else "normal"),
                      bg=(CYAN if primaer else "white"), fg=("white" if primaer else SW), relief="flat",
                      padx=14, pady=9, anchor="w", width=36, cursor="hand2").pack(fill="x", pady=4)

        knopf("📋 Medien-Check ausfuehren + Status oeffnen", self.check, primaer=True)
        knopf("🔄 Medien-Sync (04_Medien -> App)", lambda: self.skript("sync_medien.py"))
        knopf("🖼 Storyboards neu generieren", lambda: self.skript("storyboard_generator.py"))
        knopf("🔥 Marker-Heatmap neu erzeugen", lambda: self.skript("heatmap_erzeugen.py"))
        knopf("🧩 Marker erstellen (Konsole)", self.marker)
        knopf("🌐 App lokal starten (Edge)", self.app_starten)
        knopf("📦 Abgabe-Snapshot (Root -> 03_Prototyp_Code)", lambda: self.skript("abgabe_snapshot.py"))
        knopf("📓 Checkprotokoll oeffnen", lambda: self.oeffnen(ABGABE / "09_Verwaltung" / "CHECKPROTOKOLL.md"))
        knopf("🗒 Morgen-Checkliste oeffnen", lambda: self.oeffnen(ABGABE / "MORGEN_CHECKLISTE.txt"))
        self.schreibe("Bereit.")

    def schreibe(self, text):
        self.log.insert("end", text + "\n"); self.log.see("end"); self.update_idletasks()

    def oeffnen(self, pfad):
        pfad = Path(pfad)
        if not pfad.exists(): self.schreibe("Fehlt: " + str(pfad)); return
        try: os.startfile(str(pfad))
        except AttributeError: subprocess.Popen(["xdg-open", str(pfad)])

    def skript(self, name):
        def arbeit():
            self.schreibe(name + " laeuft ...")
            r = subprocess.run([sys.executable, str(REPO / "werkzeuge" / name)], capture_output=True, text=True)
            aus = (r.stdout or "") + (r.stderr or "")
            self.schreibe(aus[-1500:] if aus else "(fertig, keine Ausgabe)")
        threading.Thread(target=arbeit, daemon=True).start()

    def check(self):
        def arbeit():
            self.schreibe("Medien-Check laeuft ...")
            r = subprocess.run([sys.executable, str(ABGABE / "04_Medien" / "medien_check.py")], capture_output=True, text=True)
            self.schreibe(((r.stdout or "") + (r.stderr or ""))[-800:])
            webbrowser.open((ABGABE / "04_Medien" / "MEDIEN_STATUS.html").as_uri())
        threading.Thread(target=arbeit, daemon=True).start()

    def marker(self):
        flags = subprocess.CREATE_NEW_CONSOLE if os.name == "nt" else 0
        subprocess.Popen([sys.executable, str(REPO / "werkzeuge" / "marker_erstellen.py")], creationflags=flags)
        self.schreibe("Marker-Werkzeug in eigenem Fenster gestartet.")

    def app_starten(self):
        flags = subprocess.CREATE_NEW_CONSOLE if os.name == "nt" else 0
        subprocess.Popen([sys.executable, str(REPO / "werkzeuge" / "lokal_server.py")], creationflags=flags)
        webbrowser.open("http://localhost:8000/index_v2.html")
        self.schreibe("Server laeuft, Browser offen.")

if __name__ == "__main__":
    Cockpit().mainloop()
