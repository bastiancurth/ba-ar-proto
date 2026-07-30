# -*- coding: utf-8 -*-
"""
WERKSTATT: grafische Oberflaeche fuer alle Werkzeuge (fuer Laien gebaut)
========================================================================
Start: WERKSTATT.bat doppelklicken. Keine Kommandozeile noetig.

Was sie kann:
- Gefuehrter Assistent "Neues Werk erstellen" (mit Links zu Dreamina,
  ElevenLabs, ChatGPT und den richtigen Ablageorten)
- Video komprimieren (Web-tauglich), Idle komprimieren (stumm!),
  Audio zu MP3 wandeln, Bilder verkleinern
- Marker erstellen, Medien-Sync, Status oeffnen: alles per Knopf
"""
import os, sys, shutil, subprocess, threading, webbrowser
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

REPO = Path(__file__).resolve().parent.parent
MEDIEN = REPO / "Abgabe_Masterarbeit_Curth" / "04_Medien"
CYAN = "#00BAE5"; DUNKEL = "#0090b3"; HELL = "#f2f7f9"; SW = "#1c2733"

def ffmpeg_da():
    return shutil.which("ffmpeg") is not None

def lauf(cmd):
    """Kommando ausfuehren, Ausgabe als Text zurueck."""
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, (r.stdout or "") + (r.stderr or "")

class Werkstatt(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Werkstatt für die Redaktion: Das lebendige Bild")
        self.geometry("980x640")
        self.configure(bg=HELL)
        kopf = tk.Label(self, text="Werkstatt für die Redaktion", font=("Segoe UI", 22, "bold"),
                        bg=HELL, fg=SW)
        kopf.pack(anchor="w", padx=18, pady=(14, 0))
        tk.Label(self, text="Neue Werke erstellen und pflegen, ganz ohne Programmier- oder Kommandozeilen-Kenntnisse.",
                 font=("Segoe UI", 11), bg=HELL, fg="#5c6f7d").pack(anchor="w", padx=18)

        rahmen = tk.Frame(self, bg=HELL); rahmen.pack(fill="both", expand=True, padx=14, pady=10)
        links = tk.Frame(rahmen, bg=HELL); links.pack(side="left", fill="y", padx=(0, 10))

        def knopf(text, cmd, primaer=False):
            b = tk.Button(links, text=text, command=cmd, font=("Segoe UI", 11, "bold" if primaer else "normal"),
                          bg=(CYAN if primaer else "white"), fg=("white" if primaer else SW),
                          activebackground=DUNKEL, relief="flat", padx=14, pady=9,
                          anchor="w", width=34, cursor="hand2")
            b.pack(fill="x", pady=4)
            return b

        knopf("🧙 Neues Werk erstellen (Assistent)", self.assistent, primaer=True)
        tk.Label(links, text="Einzel-Werkzeuge", font=("Segoe UI", 10, "bold"),
                 bg=HELL, fg="#5c6f7d").pack(anchor="w", pady=(10, 2))
        knopf("🎬 Video komprimieren (mit Ton)", lambda: self.video_komprimieren(idle=False))
        knopf("🔇 Idle-Video komprimieren (stumm)", lambda: self.video_komprimieren(idle=True))
        knopf("🎙 Audio zu MP3 wandeln", self.audio_komprimieren)
        knopf("🖼 Bild verkleinern (Web-tauglich)", self.bild_komprimieren)
        tk.Label(links, text="Projekt", font=("Segoe UI", 10, "bold"),
                 bg=HELL, fg="#5c6f7d").pack(anchor="w", pady=(10, 2))
        knopf("🔥 Bild auf Marker-Eignung pruefen", self.eignung)
        knopf("🧩 Marker erstellen", self.marker)
        knopf("📖 Anleitung: Werk hinzufuegen (Text)", lambda: self.oeffnen(REPO / "WERK_HINZUFUEGEN.txt"))
        knopf("🤖 KI-Skripte: AnythingLLM-Anleitung", lambda: self.oeffnen(REPO / "Abgabe_Masterarbeit_Curth" / "05_Geschichtenerzaehler" / "Anleitung_Geschichtenerzaehler_ABGABE.docx"))
        knopf("🌐 App lokal starten", self.app_starten)

        rechts = tk.Frame(rahmen, bg=HELL); rechts.pack(side="left", fill="both", expand=True)
        self.log = tk.Text(rechts, bg="white", fg=SW, font=("Consolas", 10),
                           relief="flat", wrap="word", height=12)
        self.log.pack(fill="both", expand=True)
        tk.Label(rechts, text="Kurzanleitung: ein neues Werk erstellen", font=("Segoe UI", 11, "bold"),
                 bg=HELL, fg=SW).pack(anchor="w", pady=(8, 2))
        self.anleitung = tk.Text(rechts, bg="#eef6f9", fg=SW, font=("Segoe UI", 10),
                                 relief="flat", wrap="word", height=15, padx=10, pady=8)
        self.anleitung.pack(fill="both")
        self.anleitung_fuellen()
        self.schreibe("Bereit. Tipp: Fuer ein neues Werk einfach oben den Assistenten starten.")
        if not ffmpeg_da():
            self.schreibe("ACHTUNG: ffmpeg fehlt. Einmalig installieren: winget install --id Gyan.FFmpeg")

    def anleitung_fuellen(self):
        a = self.anleitung
        self._linkzahl = 0
        def txt(s, fett=False):
            a.insert("end", s, "fett" if fett else "")
        def link(label, url):
            self._linkzahl += 1
            tag = "link%d" % self._linkzahl
            a.insert("end", label, tag)
            a.tag_config(tag, foreground="#0090b3", underline=True)
            a.tag_bind(tag, "<Button-1>", lambda e, u=url: webbrowser.open(u))
            a.tag_bind(tag, "<Enter>", lambda e: a.config(cursor="hand2"))
            a.tag_bind(tag, "<Leave>", lambda e: a.config(cursor=""))
        a.tag_config("fett", font=("Segoe UI", 10, "bold"))
        txt("1. Bild besorgen (Rechte klaeren!), mit dem Bild-Werkzeug verkleinern und per Eignungs-Check pruefen.\n")
        txt("2. Konzeptbilder in ", ); link("ChatGPT", "https://chatgpt.com"); txt(": Befehl etwa so: ", )
        txt("\u201eBearbeite das hochgeladene Bild: <was passieren soll>. Behalte Stil und Material des Originals bei; Seitenverhaeltnis unveraendert lassen.\u201c\n", True)
        txt("3. Video in ", ); link("Dreamina (Seedance)", "https://dreamina.capcut.com"); txt(": Ausgangsbild als Start- UND Endframe hochladen. Prompt hat vier Teile: ")
        txt("Szene und Stil, Zeitachse in Sekunden-Beats, Sprechzeilen OHNE Umlaute, Loop-Regel (\u201eletztes Bild entspricht exakt dem hochgeladenen Bild\u201c).", True)
        txt(" Fertige Muster: 04_Medien/05_Seedance_Prompts.\n")
        txt("4. Stimme in ", ); link("ElevenLabs", "https://elevenlabs.io"); txt(": EINE feste Stimme je Werk (in 04_Audio_final/STIMMEN.txt eintragen). Sprechtext deutsch, Regie-Tags ENGLISCH: ")
        txt("[warm] [pause] [dry] [excited]", True)
        txt(". Erst Video-Sprechtext, dann Vorlesen-Text, dann Chat-Antworten.\n")
        txt("5. Ton ersetzen im Schnitt (z. B. ", ); link("CapCut", "https://www.capcut.com"); txt("): Seedance-Ton raus, ElevenLabs-Spur rein; Export, dann hier komprimieren (Idle stumm!).\n")
        txt("6. Marker erstellen (Knopf links; Ziel: Confidence 4 von 5 oder besser).\n")
        txt("7. Dateien ablegen wie im Assistenten beschrieben, in werke.js die Zeile inProduktion loeschen, App lokal testen. ")
        txt("Jede Faktenaussage vor Freischaltung gegen die Originalquellen pruefen!", True)
        a.configure(state="disabled")

    # ---------- Helfer ----------
    def schreibe(self, text):
        self.log.insert("end", text + "\n"); self.log.see("end"); self.update_idletasks()

    def oeffnen(self, pfad):
        pfad = Path(pfad)
        if not pfad.exists():
            self.schreibe("Datei nicht gefunden: " + str(pfad)); return
        try:
            os.startfile(str(pfad))            # Windows
        except AttributeError:
            subprocess.Popen(["xdg-open", str(pfad)])
        self.schreibe("Geoeffnet: " + pfad.name)

    def im_hintergrund(self, funktion):
        threading.Thread(target=funktion, daemon=True).start()

    # ---------- Einzelwerkzeuge ----------
    def video_komprimieren(self, idle=False):
        q = filedialog.askopenfilename(title="Video waehlen", filetypes=[("Video", "*.mp4 *.mov *.webm *.mkv")])
        if not q: return
        ziel = str(Path(q).with_name(Path(q).stem + ("_idle_web" if idle else "_web") + ".mp4"))
        def arbeit():
            self.schreibe(("Idle (stumm)" if idle else "Video") + " wird komprimiert: " + Path(q).name + " ...")
            cmd = ["ffmpeg", "-y", "-i", q, "-c:v", "libx264", "-crf", "28" if idle else "27",
                   "-preset", "fast", "-vf", "scale='min(960,iw)':-2", "-pix_fmt", "yuv420p",
                   "-movflags", "+faststart"]
            cmd += ["-an"] if idle else ["-c:a", "aac", "-b:a", "96k"]
            code, aus = lauf(cmd + [ziel])
            if code == 0:
                mb = os.path.getsize(ziel) / 1e6
                self.schreibe(f"Fertig: {ziel}  ({mb:.1f} MB)")
                self.schreibe("Ablage: 04_Medien/03_Videos_final/<werk>/<werk>" + ("_idle" if idle else "") + ".mp4, dann Medien-Sync.")
            else:
                self.schreibe("FEHLER:\n" + aus[-400:])
        self.im_hintergrund(arbeit)

    def audio_komprimieren(self):
        dateien = filedialog.askopenfilenames(title="Audio waehlen (mehrere moeglich)",
                  filetypes=[("Audio", "*.mp3 *.wav *.m4a *.aac *.ogg *.flac")])
        if not dateien: return
        def arbeit():
            for q in dateien:
                ziel = str(Path(q).with_suffix("")) + "_web.mp3"
                self.schreibe("Audio wird gewandelt: " + Path(q).name + " ...")
                code, aus = lauf(["ffmpeg", "-y", "-i", q, "-c:a", "libmp3lame", "-b:a", "112k", "-ar", "44100", ziel])
                if code == 0:
                    self.schreibe(f"Fertig: {ziel}  ({os.path.getsize(ziel)/1e6:.2f} MB)")
                else:
                    self.schreibe("FEHLER:\n" + aus[-300:])
            self.schreibe("Ablage: Vorlesen -> 04_Medien/04_Audio_final/<werk>/<werk>.mp3; Antworten -> assets/audio/antworten/.")
        self.im_hintergrund(arbeit)

    def bild_komprimieren(self):
        dateien = filedialog.askopenfilenames(title="Bilder waehlen (mehrere moeglich)",
                  filetypes=[("Bilder", "*.jpg *.jpeg *.png *.webp *.tif *.tiff")])
        if not dateien: return
        def arbeit():
            try:
                from PIL import Image
            except ImportError:
                self.schreibe("Pillow fehlt. Einmalig: pip install pillow"); return
            for q in dateien:
                im = Image.open(q); im.load()
                if im.mode in ("RGBA", "P") and Path(q).suffix.lower() in (".jpg", ".jpeg"):
                    im = im.convert("RGB")
                im.thumbnail((1600, 1600), Image.LANCZOS)
                ziel = str(Path(q).with_suffix("")) + "_web" + Path(q).suffix.lower().replace(".jpeg", ".jpg")
                if ziel.endswith((".tif", ".tiff", ".webp")): ziel = str(Path(ziel).with_suffix(".jpg")); im = im.convert("RGB")
                im.save(ziel, quality=84)
                self.schreibe(f"Fertig: {ziel}  ({os.path.getsize(ziel)/1e3:.0f} kB)")
            self.schreibe("Ausgangsbilder -> 04_Medien/01_Ausgangsbilder/<werk>/; App-Bilder -> assets/bilder/.")
        self.im_hintergrund(arbeit)

    def eignung(self):
        q = filedialog.askopenfilename(title="Bild waehlen", filetypes=[("Bilder", "*.jpg *.jpeg *.png *.webp *.tif *.tiff")])
        if not q: return
        def arbeit():
            try:
                from PIL import Image, ImageDraw
            except ImportError:
                self.schreibe("Pillow fehlt. Einmalig: pip install pillow"); return
            im = Image.open(q).convert("RGB"); B, H = im.size
            self.schreibe(f"Pruefe {Path(q).name} ({B}x{H} px) ...")
            hinweise = []
            kurz = min(B, H)
            if kurz < 480: hinweise.append("ZU KLEIN: kurze Kante unter 480 px, Tracking wird unzuverlaessig.")
            elif kurz < 1000: hinweise.append("Aufloesung knapp: der Guide empfiehlt mindestens 1000 px kurze Kante.")
            else: hinweise.append("Aufloesung gut (kurze Kante %d px)." % kurz)
            seite = max(B, H) / kurz
            if seite > 2.2: hinweise.append("Sehr laengliches Format (%.1f:1): fuer Druck und Buehne unpraktisch." % seite)
            try:
                import cv2, numpy as np
                grau = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2GRAY)
                ecken = cv2.goodFeaturesToTrack(grau, maxCorners=400, qualityLevel=0.03, minDistance=max(6, kurz // 90))
                punkte = [] if ecken is None else [tuple(e) for e in ecken.reshape(-1, 2)]
                raster, leer = 4, 0
                for gy in range(raster):
                    for gx in range(raster):
                        n = sum(1 for x, y in punkte
                                if gx * B / raster <= x < (gx + 1) * B / raster and gy * H / raster <= y < (gy + 1) * H / raster)
                        if n < 3: leer += 1
                if len(punkte) < 80: hinweise.append("WENIG MERKMALE (%d Punkte): kontrastarmes Motiv, Tracking fraglich." % len(punkte))
                elif leer >= 6: hinweise.append("%d Merkmale, aber %d von 16 Zonen fast leer: grosse strukturarme Flaechen." % (len(punkte), leer))
                else: hinweise.append("Merkmalsdichte gut: %d Punkte, flaechig verteilt." % len(punkte))
                # Heatmap-Bild erzeugen
                heat = np.zeros((H, B), np.float32)
                for x, y in punkte: cv2.circle(heat, (int(x), int(y)), max(8, kurz // 60), 1.0, -1)
                heat = cv2.GaussianBlur(heat, (0, 0), max(10, kurz // 50))
                if heat.max() > 0: heat = heat / heat.max()
                farbe = cv2.applyColorMap((heat * 255).astype(np.uint8), cv2.COLORMAP_TURBO)
                mix = cv2.addWeighted(cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR), 0.6, farbe, 0.4, 0)
                for x, y in punkte:
                    cv2.drawMarker(mix, (int(x), int(y)), (40, 255, 90), cv2.MARKER_CROSS, 7, 1)
                ziel = str(Path(q).with_suffix("")) + "_eignung.png"
                cv2.imwrite(ziel, mix)
                self.schreibe("Heatmap gespeichert: " + ziel)
                self.oeffnen(ziel)
            except ImportError:
                hinweise.append("(Fuer die Heatmap einmalig: pip install opencv-python-headless numpy)")
            for h in hinweise: self.schreibe("  - " + h)
            self.schreibe("Endgueltiges Mass ist die Confidence beim Marker-Erstellen (Ziel: 4 von 5 oder besser).")
        self.im_hintergrund(arbeit)

    def marker(self):
        self.schreibe("Marker-Werkzeug startet in eigenem Fenster (fragt nach dem Werk) ...")
        flags = subprocess.CREATE_NEW_CONSOLE if os.name == "nt" else 0
        subprocess.Popen([sys.executable, str(REPO / "werkzeuge" / "marker_erstellen.py")], creationflags=flags)

    def sync(self):
        def arbeit():
            self.schreibe("Medien-Sync laeuft ...")
            code, aus = lauf([sys.executable, str(REPO / "werkzeuge" / "sync_medien.py")])
            self.schreibe(aus[-1200:] if aus else "(keine Ausgabe)")
        self.im_hintergrund(arbeit)

    def app_starten(self):
        flags = subprocess.CREATE_NEW_CONSOLE if os.name == "nt" else 0
        subprocess.Popen([sys.executable, str(REPO / "werkzeuge" / "lokal_server.py")], creationflags=flags)
        webbrowser.open("http://localhost:8000/index_v2.html")
        self.schreibe("Lokaler Server gestartet, Browser geoeffnet (Fenster mit dem Server offen lassen).")

    # ---------- Assistent ----------
    def assistent(self):
        w = tk.Toplevel(self); w.title("Neues Werk erstellen"); w.geometry("860x600"); w.configure(bg="white")
        tk.Label(w, text="Neues Werk in 7 Schritten", font=("Segoe UI", 16, "bold"), bg="white", fg=SW).pack(anchor="w", padx=16, pady=(12, 2))
        zeile = tk.Frame(w, bg="white"); zeile.pack(anchor="w", padx=16)
        tk.Label(zeile, text="Werk-Kennung (klein, keine Umlaute, z. B. dom):", bg="white", font=("Segoe UI", 11)).pack(side="left")
        kennung = tk.Entry(zeile, font=("Segoe UI", 11), width=18); kennung.pack(side="left", padx=8)

        text = tk.Text(w, bg="white", fg=SW, font=("Segoe UI", 10.5), relief="flat", wrap="word", height=18)
        text.pack(fill="both", expand=True, padx=16, pady=8)
        text.insert("end",
            "1. ORDNER ANLEGEN: Knopf unten erzeugt die komplette Ordnerstruktur fuer das Werk und kopiert dir den werke.js-Baustein in die Zwischenablage (in werke.js VOR dem letzten ] einfuegen).\n\n"
            "2. AUSGANGSBILD: hochaufloesendes Bild besorgen (Rechte klaeren!), mit dem Bild-Werkzeug verkleinern, ablegen als 01_Ausgangsbilder/<werk>/<werk>.jpg UND assets/bilder/<werk>.jpg.\n\n"
            "3. GESCHICHTE UND PROMPTS, zwei Wege:\n"
            "   Weg A (selbst schreiben): Geschichte, Fakten und Chat-Antworten von Hand verfassen; Vorbild ist jedes bestehende Werk in werke.js.\n"
            "   Weg B (KI-Entwurf): Quellen sammeln, in AnythingLLM als Workspace laden (Systemprompt liegt in 05_Geschichtenerzaehler/systemprompt.txt), Entwurf generieren lassen. PFLICHT: Jede Faktenaussage gegen die Originalquellen pruefen und das Feld wahrErzaehlt ehrlich fuellen; die KI liefert nur den Entwurf! (Anleitung: Knopf links.)\n"
            "   Danach den Seedance-Prompt nach dem Muster in 04_Medien/05_Seedance_Prompts bauen (vier Bausteine: Szene, Beats, umlautfreie Sprechzeilen, Loop-Regel).\n\n"
            "4. VIDEO: In Dreamina generieren (Ausgangsbild als Start- UND Endframe). Rohfassungen nach 03_Videos_final/<werk>/roh/. In CapCut Ton ersetzen, Export, dann hier mit dem Video-Werkzeug komprimieren; Idle stumm erzeugen.\n\n"
            "5. STIMME: In ElevenLabs eine feste Stimme waehlen (in 04_Audio_final/STIMMEN.txt eintragen!). Video-Sprechtext, Vorlesen-Text und Chat-Antworten einsprechen; Tags englisch. Mit dem Audio-Werkzeug wandeln und ablegen.\n\n"
            "6. MARKER: Knopf 'Marker erstellen' (Confidence 4+ anstreben).\n\n"
            "7. FREISCHALTEN: Medien-Sync ausfuehren, in werke.js die Zeile inProduktion: true loeschen, App lokal testen. Fertig!\n")
        text.configure(state="disabled")

        leiste = tk.Frame(w, bg="white"); leiste.pack(fill="x", padx=16, pady=(0, 12))
        def anlegen():
            wid = kennung.get().strip().lower()
            if not wid.isidentifier() or not wid.isascii():
                messagebox.showerror("Werkstatt", "Bitte eine einfache Kennung ohne Umlaute/Leerzeichen."); return
            for d in [MEDIEN / "01_Ausgangsbilder" / wid,
                      MEDIEN / "02_Generierte_Frames" / wid / "kurzclip_beats",
                      MEDIEN / "03_Videos_final" / wid / "roh",
                      MEDIEN / "04_Audio_final" / wid,
                      MEDIEN / "06_Marker_NFT" / wid]:
                d.mkdir(parents=True, exist_ok=True)
            baustein = (
                '  {\n'
                f'    id: "{wid}",\n'
                f'    titel: "NEUES WERK {wid}",\n'
                '    untertitel: "",\n'
                '    inProduktion: true,\n'
                f'    marker: "assets/markers/{wid}/{wid}",\n'
                f'    video:  "assets/videos/{wid}.mp4",\n'
                f'    // videoIdle: "assets/videos/{wid}_idle.mp4",\n'
                f'    audio:  "assets/audio/{wid}.mp3",\n'
                f'    bild:   "assets/bilder/{wid}.jpg",\n'
                f'    freihandBild: "assets/bilder/freihand_{wid}.png",\n'
                '    kalibrierung: { position: "0 0 -20", rotation: "-90 0 0", scale: "20 20 20" },\n'
                '    geschichte: "",\n'
                '    wahrErzaehlt: "",\n'
                '    fakten: [],\n'
                '    quellen: [],\n'
                '    dialog: []\n'
                '  },')
            w.clipboard_clear(); w.clipboard_append(baustein)
            messagebox.showinfo("Werkstatt", f"Ordner fuer '{wid}' angelegt.\nwerke.js-Baustein liegt in der Zwischenablage.")
        tk.Button(leiste, text="Schritt 1: Ordner anlegen + Baustein kopieren", command=anlegen,
                  bg=CYAN, fg="white", relief="flat", font=("Segoe UI", 11, "bold"), padx=12, pady=8).pack(side="left")
        for label, url in (("Dreamina oeffnen", "https://dreamina.capcut.com"),
                            ("ElevenLabs oeffnen", "https://elevenlabs.io"),
                            ("ChatGPT oeffnen", "https://chatgpt.com")):
            tk.Button(leiste, text=label, command=lambda u=url: webbrowser.open(u),
                      bg="white", fg=SW, relief="groove", font=("Segoe UI", 10), padx=10, pady=7).pack(side="left", padx=6)

if __name__ == "__main__":
    Werkstatt().mainloop()
