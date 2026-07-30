# Das lebendige Bild

Web-AR-Prototyp der Masterarbeit "Konzeption und prototypische Umsetzung eines
GenAI-gestuetzten Web-AR-Erlebnisses fuer historische Bildmedien"
(Bastian Curth, Technische Hochschule Brandenburg, 2026).

Historische Bilder und Kunstwerke werden mit dem Handy gescannt und erwachen
als kurze, KI-generierte Videogeschichten zum Leben. Dazu gibt es Vorlesen-Texte,
einen Frage-Chat je Werk und eine Kennzeichnung, was belegt und was erzaehlt ist.

## Ausprobieren

* Online (Handy, empfohlen): die GitHub-Pages-URL dieses Repos oeffnen und
  "AR-Erlebnis" waehlen. Die Kamera braucht HTTPS, deshalb funktioniert der
  Kamera-Modus nur online oder ueber localhost.
* Ohne Kamera: Menuepunkt "Lexikon" oder ein Werk im Demo-Modus oeffnen.
* Lokal (Windows): `LOKAL_STARTEN.bat` doppelklicken (startet einen lokalen
  Server mit Range-Support und oeffnet Edge auf `http://localhost:8000/index_v2.html`).
* Galerie-Modus: ein Rechner zeigt die Werke auf dem Monitor, Handys scannen
  den Bildschirm.

## Aufbau

* `index_v2.html` – die komplette App (eine Datei, kein Build-Schritt)
* `werke.js` – Inhalte aller Werke (Geschichten, Fakten, Chat-Antworten)
* `assets/` – Bilder, Videos, Audios und NFT-Marker
* `werkzeuge/` – Werkstatt fuer die Redaktion (Kompression, Marker-Erstellung,
  Eignungs-Check, Assistent fuer neue Werke); Details in `WERK_HINZUFUEGEN.txt`
* `index_v1_monatest.html` – frueher Einzelwerk-Prototyp (Mona Lisa), nur Historie

## Technik

AR.js (NFT-Tracking) mit A-Frame; Marker erstellt mit dem
[NFT-Marker-Creator](https://github.com/Carnaux/NFT-Marker-Creator) (MIT).
Videos: Seedance 2.0 via Dreamina, Stimmen: ElevenLabs, Schnitt: CapCut.
Alle Inhalte werden redaktionell gegen Originalquellen geprueft.
