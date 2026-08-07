// ============================================================================
// WERKE.JS; Die Inhalts-Datei des digitalen Geschichtenerzählers
// ============================================================================
// Diese Datei ist so gebaut, dass sie OHNE Programmierkenntnisse gepflegt
// werden kann. Einfach mit einem Texteditor (Notepad) öffnen, UTF-8 speichern.
//
// WERK FREISCHALTEN, wenn das Video fertig ist:
//   1. Video, Audio und Marker-Dateien in die assets-Ordner legen
//      (Pfade stehen unten schon beim jeweiligen Werk)
//   2. Die Zeile   inProduktion: true,   beim Werk LÖSCHEN
//   3. Mit dem Justier-Modus kalibrieren (5x auf Statusleiste tippen,
//      Werte kopieren, unten bei "kalibrierung" einfügen)
//
// Solange inProduktion: true gesetzt ist, sind Geschichte, Fakten und Chat
// trotzdem schon nutzbar; nur das AR-Erlebnis ist ausgeblendet.
//
// Aufruf eines Werks:  index_v2.html?werk=mona   (id siehe unten)
// Kamera-Modus (erkennt selbst, welches Werk vor der Linse ist):
//   index_v2.html?modus=kamera
//
// WEITERE OPTIONALE FELDER PRO WERK:
//   bild: "assets/bilder/xy.jpg"   Standbild-Overlay, solange das Video fehlt
//   imKameraModus: false           Werk vom Kamera-Modus ausnehmen (spart Leistung)
//   videoIdle:                     stummer, nahtlos loopender Kurzclip.
//                                  Das Bild "lebt" damit still vor sich hin;
//                                  die vertonte Geschichte startet erst auf
//                                  Knopfdruck und kehrt danach in den Loop
//                                  zurueck. Zeile unten einkommentieren,
//                                  sobald die Datei da ist!
//   wahrErzaehlt:                  Kurztext "Wahr oder erzaehlt?" fuers
//                                  Info-Panel: was ist belegt, was ist
//                                  bewusste Dramatisierung. (Transparenz-
//                                  Prinzip seit dem Zwischenkolloquium.)
//   audio (beim Werk):             Erzaehlspur als MP3 fuer den Vorlesen-
//                                  Knopf an der Geschichte. Im Video selbst
//                                  ist die Stimme schon eingeschnitten!
//   audio bei Chat-Antworten:      { frage, stichworte, antwort,
//                                    audio: "assets/audio/antworten/xy.mp3" }
//                                  wird beim Antworten automatisch abgespielt
//
//   WELCHER TEXT TRAEGT DAS VIDEO? Das fertige Kurzclip-Video traegt NUR die
//                                  kurzen Sprechzeilen aus 04_Medien/
//                                  05_Seedance_Prompts/{werk}_seedance_prompt.txt
//                                  (umlautfreie Kurzfassung; Stimme ist im
//                                  Schnitt eingebacken). Die "geschichte" unten
//                                  ist der bewusst laengere Vorlesen-/Chat-Text
//                                  und bleibt lang - das ist gewollt.
//                                  Ausnahme W1 Mona: Clip-Skript und geschichte
//                                  sind dort fast identisch (Fassung 6, A.1).
// ============================================================================

const WERKE = [

  // ==========================================================================
  // WERK 1: MONA LISA  (fertig; Dateien folgen dem Schema assets/.../mona.*)
  // ==========================================================================
  {
    id: "mona",
    freihandBild: "assets/bilder/freihand_mona.png",  // Freihand-Hintergrund (Outpainting, PNG aus Photoshop; App probiert notfalls .jpg)
    freihandLage: { cx: 0.5, cy: 0.5, breite: 0.85, seite: 1.4868 },  // Hochformat: mittig, 85 % Breite; seite = Hoehe/Breite des Originals
    // Lage des Videos auf dem Hintergrund: Standard mittig bei 85 % Breite (1080x2340-Leinwand).
    // freihandLage: { cx, cy, breite, seite } = Lage/Groesse der Originalflaeche auf der 1080x2340-Leinwand
    // (relativ 0..1); seite = Hoehe/Breite des Originals. Die App schneidet das Video per object-fit auf
    // exakt diese Flaeche zu, selbst wenn Seedance ein anderes Seitenverhaeltnis liefert.
    titel: "Mona Lisa",
    untertitel: "Leonardo da Vinci, um 1503–1519 · Musée du Louvre, Paris",
    marker: "assets/markers/mona/mona",
    video:  "assets/videos/mona.mp4",
    bild:   "assets/bilder/mona.jpg",   // Standbild (Galerie-Modus, Buehne, Fallback)
    videoIdle: "assets/videos/mona_idle.mp4",   // Test-Fassung 19.07., stumm komprimiert
    audio:  "assets/audio/mona.mp3",
    kalibrierung: { position: "12 0 -48", rotation: "-90 0 0", scale: "31 31 31" },

    geschichte: "Sie wollen meine Geschichte? Nun gut, aber nur, weil Sie so nett gucken. Florenz, um 1503: Ein gewisser Leonardo da Vinci setzt den Pinsel an und braucht dann Jahre für mich. Perfektionist! Mein richtiger Name ist übrigens Lisa del Giocondo. Berühmt wurde ich durch seine Geheimwaffe: das Sfumato, diese weiche, rauchige Malweise ganz ohne harte Linien. Aber unsterblich? Das machte mich erst ein Dieb. 1911 trug mich ein Mann unter seinem Mantel aus dem Louvre, zwei Jahre war ich verschwunden, und die ganze Welt suchte nach mir. Seitdem stehe ich hinter Panzerglas und werde öfter fotografiert als jedes Supermodel. Und das, obwohl ich nicht einmal Augenbrauen habe.",

    wahrErzaehlt: "Belegt: Leonardo da Vinci als Schöpfer, die Entstehung um 1503, der Steinwurf 1956 und die Torte 2022 (Diebstahl 1911 und Suppe 2024 stecken im Chat). Erzählt: die Anrede „Papa Leonardo“, das Smartphone samt Selfie-Blick, das elegante Ausweichen und der Stein im gemalten Fluss.",

    fakten: [
      "Dargestellt ist vermutlich Lisa del Giocondo, die Frau eines Florentiner Kaufmanns.",
      "Öl auf Pappelholz, nur 77 × 53 cm groß; viele Besucher sind überrascht, wie klein das Original ist.",
      "Die berühmte weiche Malweise heißt Sfumato: hauchdünne Farbschichten ohne harte Konturen.",
      "Die Mona Lisa hat keine sichtbaren Augenbrauen.",
      "1911 stahl der Handwerker Vincenzo Peruggia das Gemälde aus dem Louvre; es blieb über zwei Jahre verschwunden. Erst dieser Diebstahl machte es weltberühmt.",
      "Heute hängt sie im Louvre (Salle des États) hinter Panzerglas."
    ],
    quellen: [
      "Musée du Louvre, Sammlungsdatenbank (collections.louvre.fr)",
      "Encyclopaedia Britannica: Mona Lisa",
      "Library of Congress: The Theft of the Mona Lisa (1911)",
      "Wikipedia: Mona Lisa"
    ],
    dialog: [
      { frage: "Warum bist du so berühmt?",
        stichworte: ["berühmt", "beruehmt", "bekannt", "ruhm"],
        antwort: "Ehrlich gesagt: durch einen Skandal. 1911 stahl mich der Handwerker Vincenzo Peruggia aus dem Louvre. Zwei Jahre war ich verschwunden, und die ganze Welt sprach über mich. Vorher war ich ein bewundertes Gemälde, danach eine Legende.",
        audio: "assets/audio/antworten/mona_antwort_1.mp3" },
      { frage: "Wer ist die Frau auf dem Bild?",
        stichworte: ["frau", "lisa", "giocondo", "name", "dargestellt"],
        antwort: "Vermutlich bin ich Lisa del Giocondo, die Frau eines Florentiner Seidenhändlers. Leonardo begann um 1503 mit dem Porträt und arbeitete viele Jahre daran.",
        audio: "assets/audio/antworten/mona_antwort_2.mp3" },
      { frage: "Warum hast du keine Augenbrauen?",
        stichworte: ["augenbrauen", "brauen", "wimpern"],
        antwort: "Das fragt jeder! Ganz sicher weiß man es nicht. Möglich ist, dass feine Härchen einst gemalt waren und über die Jahrhunderte durch Reinigungen verloren gingen.",
        audio: "assets/audio/antworten/mona_antwort_3.mp3" },
      { frage: "Wie groß bist du wirklich?",
        stichworte: ["groß", "gross", "größe", "groesse", "klein", "maße", "masse"],
        antwort: "Viele sind überrascht: nur 77 mal 53 Zentimeter, Öl auf Pappelholz. Im Louvre stehe ich hinter Panzerglas, deshalb wirke ich noch kleiner.",
        audio: "assets/audio/antworten/mona_antwort_4.mp3" },
      { frage: "Was ist Sfumato?",
        stichworte: ["sfumato", "technik", "malweise", "gemalt"],
        antwort: "Leonardos Geheimwaffe: viele hauchdünne Farbschichten ohne harte Konturen. Alles wird weich wie Rauch. Genau deshalb wirkt mein Lächeln so rätselhaft.",
        audio: "assets/audio/antworten/mona_antwort_5.mp3" },
      { frage: "Was hat es mit der Torte auf sich?",
        stichworte: ["torte", "kuchen", "beworfen", "angriff", "attacke", "stein", "suppe", "geworfen"],
        antwort: "Sie haben es also gesehen! 2022 warf mir ein als alte Dame verkleideter Mann eine Sahnetorte entgegen. Das Panzerglas hat gehalten, ich blieb unversehrt. Es war nicht der erste Wurf: 1956 traf mich ein Stein und beschädigte den Farbauftrag am Ellenbogen, 2024 kippten Aktivistinnen Suppe gegen die Scheibe. Man gewöhnt sich an alles. Nur die Sahne war ehrlich gesagt eine Zumutung.",
        audio: "assets/audio/antworten/mona_antwort_6.mp3" },
      { frage: "Warum lächelst du so?",
        stichworte: ["lächeln", "laecheln", "lächelst", "laechelst", "mundwinkel", "geheimnis", "rätselhaft"],
        antwort: "Weil ich die Frage seit fünfhundert Jahren höre und immer noch nichts verrate. Der Trick steckt in Leonardos weicher Malweise: Meine Mundwinkel sind bewusst unscharf gehalten. Schauen Sie mir in die Augen, lächle ich deutlich. Schauen Sie direkt auf meinen Mund, verschwindet es fast. Nicht ich ändere mich, sondern Ihr Blick.",
        audio: "assets/audio/antworten/mona_antwort_7.mp3" }
    ],
    kiHinweis: true
  },

  // ==========================================================================
  // WERK 2: LORIOT  (erzaehlt selbst; der Waldmops ist nur sein Gast)
  // ==========================================================================
  {
    id: "loriot",
    freihandBild: "assets/bilder/freihand_loriot.png",  // Freihand-Hintergrund (Outpainting, PNG aus Photoshop; App probiert notfalls .jpg)
    freihandLage: { cx: 0.5, cy: 0.5, breite: 1.0, seite: 0.7506 },  // Querformat: volle 1080-px-Breite; seite = Hoehe/Breite des Originals
    // Sichtbar ist die Waldmops-Skulptur, deshalb traegt das Werk ihren Namen.
    // Loriot bleibt der Erzaehler und wird im Untertitel und in der Geschichte genannt.
    titel: "Waldmops",
    untertitel: "Bronzefigur nach Loriots Erfindung, Clara Walter, seit 2015 · erzählt von Loriot (Vicco von Bülow, 1923 bis 2011)",
    // inProduktion entfernt am 19.07.2026: Video + Idle sind fertig und komprimiert in assets/videos/
    marker: "assets/markers/loriot/loriot",
    video:  "assets/videos/loriot.mp4",
    videoIdle: "assets/videos/loriot_idle.mp4",   // stummer 5-s-Loop (komprimiert, ohne Tonspur)
    audio:  "assets/audio/loriot.mp3",
    bild:   "assets/bilder/loriot.jpg",   // Standbild-Fallback (Datei noch ablegen)
    kalibrierung: { position: "0 0 -20", rotation: "-90 0 0", scale: "20 20 20" },

    // Diese Geschichte stammt aus der lokalen Ollama/AnythingLLM-Pipeline
    // (gemma3:4b, Anfrage mit vorgegebenem Fakten-Geruest) und wurde am
    // 02.07.2026 redaktionell gekuerzt. Beleg: Abgabe-Ordner 05, Erfolgsfall.
    geschichte: "Guten Tag. Der Waldmops: wild lebend, sehr selten, bitte nicht füttern. Man erkennt ihn am kleinen Geweih. Ich habe ihn erfunden, und ich wurde am 12. November 1923 genau hier geboren, in Brandenburg an der Havel. Zu meinen Ehren hat die Künstlerin Clara Walter siebenundzwanzig von ihnen in Bronze gegossen und in der Stadt ausgewildert. Sie gelten als standorttreu. Meistens. Ich wusste stets um ihre Bedeutung, schließlich stammt von mir der Satz, ein Leben ohne Mops sei möglich, aber sinnlos. Wenn Sie durch die Stadt gehen, zählen Sie sie ruhig. Und sollte einer fehlen, sagen Sie bitte nichts. Er kommt bestimmt gleich wieder.",

    wahrErzaehlt: "Belegt: Geburt 1923 in Brandenburg, der Tierstunde-Sketch von 1972, die 27 ausgewilderten Bronzemöpse nach Entwürfen von Clara Walter. Erzählt: die Warnung und das Fütterungsverbot. Kern des Textes stammt aus der lokalen KI-Pipeline und wurde redaktionell erweitert.",

    fakten: [
      "Loriot wurde am 12. November 1923 im städtischen Krankenhaus in Brandenburg an der Havel geboren und am 30. Dezember 1923 in der St.-Gotthardt-Kirche getauft.",
      "Loriot ist Französisch für Pirol, das Wappentier der Familie von Bülow.",
      "Der Sketch \'Tierstunde: Der wilde Waldmops\' von 1972 nimmt den Züchterehrgeiz aufs Korn: Aus dem gehörnten Wildtier sei der Schoßhund gezüchtet worden.",
      "Zur Bundesgartenschau 2015 wurden die ersten bronzenen Waldmops-Figuren der Künstlerin Clara Walter in der Innenstadt aufgestellt.",
      "Heute sind 27 Waldmöpse in den drei historischen Stadtkernen ausgewildert; 2021 wurde die Waldmops-Bande der Stadt geschenkt.",
      "Loriot ist Ehrenbürger der Stadt Brandenburg an der Havel."
    ],
    quellen: [
      "Stadt Brandenburg an der Havel, Pressemitteilung zur Waldmops-Bande (stadt-brandenburg.de)",
      "Erlebnis Brandenburg: Loriot und die Waldmöpse (erlebnis-brandenburg.de/loriot)",
      "Kulturnotizen: Loriot, ein Sohn der Stadt Brandenburg an der Havel",
      "Wikipedia: Vicco von Bülow, Waldmöpse",
      "Foto der Waldmops-Skulptur: Gregor Rom, Wikimedia Commons, CC BY-SA 4.0. Skulptur: Clara Walter (§ 59 UrhG)"
    ],
    dialog: [
      { frage: "Was ist ein Waldmops?",
        stichworte: ["waldmops", "geweih", "hörner", "hoerner", "wildtier"],
        antwort: "Eine meiner schönsten Erfindungen! 1972 habe ich in der Tierstunde behauptet, der Mops stamme vom wilden Waldmops ab, einem scheuen Wildtier mit kleinem Geweih. Erst der Ehrgeiz der Züchter habe daraus den Schoßhund gemacht. Reine Wissenschaft, versteht sich.",
        audio: "assets/audio/antworten/loriot_antwort_1.mp3" },
      { frage: "Wo finde ich die anderen Möpse?",
        stichworte: ["finde", "standorte", "karte", "möpse", "moepse", "viele"],
        antwort: "27 meiner Bronze-Möpse sind in der Innenstadt ausgewildert, unter anderem an der Johanniskirche, am Havelpegel und auf dem Altstädtischen Markt. Die Stadt hat sogar eine eigene Waldmops-Karte zum Herunterladen.",
        audio: "assets/audio/antworten/loriot_antwort_2.mp3" },
      { frage: "Was verbindet dich mit Brandenburg?",
        stichworte: ["brandenburg", "geboren", "stadt", "heimat", "verbindet"],
        antwort: "Hier fing alles an: geboren am 12. November 1923 im städtischen Krankenhaus, getauft in der St.-Gotthardt-Kirche. Meine ersten vier Lebensjahre verbrachte ich in dieser Stadt, und heute bin ich ihr Ehrenbürger.",
        audio: "assets/audio/antworten/loriot_antwort_3.mp3" },
      { frage: "Warum heißt du Loriot?",
        stichworte: ["loriot", "heißt", "heisst", "pseudonym", "pirol"],
        antwort: "Loriot ist Französisch für Pirol. Der Pirol ist das Wappentier meiner Familie, derer von Bülow. Klingt eleganter als Vogel, finden Sie nicht?",
        audio: "assets/audio/antworten/loriot_antwort_4.mp3" },
      { frage: "Wer hat die Skulpturen gemacht?",
        stichworte: ["skulptur", "bronze", "künstler", "kuenstler", "gemacht", "walter"],
        antwort: "Die Künstlerin Clara Walter hat die Waldmöpse geschaffen. Die ersten wurden 2015 zur Bundesgartenschau aufgestellt, 2021 wurde die ganze Bande der Stadt geschenkt.",
        audio: "assets/audio/antworten/loriot_antwort_5.mp3" },
      { frage: "Darf man die Möpse füttern?",
        stichworte: ["füttern", "fuettern", "futter", "fütterung", "fuetterung", "essen geben", "leckerli"],
        antwort: "Auf gar keinen Fall. Der Waldmops ist ein Wildtier und ernährt sich selbstständig, vorzugsweise von dem, was unter Parkbänken liegt. Wer ihn füttert, macht ihn zutraulich, und ein zutraulicher Waldmops ist ein Mops, der auf Fototermine besteht. Bitte beobachten Sie ihn aus respektvoller Entfernung.",
        audio: "assets/audio/antworten/loriot_antwort_6.mp3" },
      { frage: "Haben Waldmöpse wirklich ein Geweih?",
        stichworte: ["wirklich ein geweih", "echtes geweih", "merkmal", "aussehen", "gehörnt", "gehoernt"],
        antwort: "Ein kleines, ja. Genau daran erkennt man ihn, und genau darum ging es 1972 in meiner Tierstunde: Der Züchterehrgeiz hat aus dem gehörnten Wildtier den Schoßhund gemacht. Ein Jammer. Betrachten Sie das Geweih also mit dem gebotenen Respekt. Es ist alles, was dem Waldmops von seiner wilden Vergangenheit geblieben ist.",
        audio: "assets/audio/antworten/loriot_antwort_7.mp3" }
    ],
    kiHinweis: true
  },

  // ==========================================================================
  // WERK 3: FRITZ-KNITTER-ZEICHNUNG  (Video in Produktion)
  // ==========================================================================
  {
    id: "knitter",
    freihandBild: "assets/bilder/freihand_knitter.png",  // Freihand-Hintergrund (Outpainting, PNG aus Photoshop; App probiert notfalls .jpg)
    freihandLage: { cx: 0.5, cy: 0.5, breite: 1.0, seite: 0.7508 },  // Querformat: volle 1080-px-Breite; seite = Hoehe/Breite des Originals
    titel: "Frauen auf einer Bank",
    untertitel: "Fritz Knitter, 1930er-Jahre · Stadtmuseum Brandenburg im Frey-Haus",
    // inProduktion entfernt am 19.07.2026: Test-Fassungen (roh final + idle) sind in der App
    marker: "assets/markers/knitter/knitter",
    video:  "assets/videos/knitter.mp4",
    videoIdle: "assets/videos/knitter_idle.mp4",   // Test-Fassung 19.07., stumm komprimiert
    audio:  "assets/audio/knitter.mp3",
    bild:   "assets/bilder/knitter.jpg",   // Standbild-Fallback (Datei noch ablegen)
    kalibrierung: { position: "0 0 -20", rotation: "-90 0 0", scale: "20 20 20" },

    geschichte: "Pssst, kommen Sie näher, wir erzählen es auch nur Ihnen. Der Mann, der uns gezeichnet hat, hieß Fritz Knitter. Ein Brandenburger mit spitzer Feder: erst Beamter, später städtischer Arbeiter, und gezeichnet hat er trotzdem immer. Manchmal, so erzählt man sich, sogar auf Verpackungspapier. Die Leute vergleichen ihn gern mit dem Zille aus Berlin, weil er wie der den kleinen Leuten aufs Maul und auf die Hüte geschaut hat. Uns hat er um 1930 auf diese Bank gesetzt, zum ewigen Tratschen. Heute hängen wir im Stadtmuseum im Frey-Haus. Und wissen Sie was? Kennen tut ihn kaum noch jemand. Dabei sitzen wir auf dem besten Beweis: auf seiner Bank.",

    wahrErzaehlt: "Belegt: die Zeichnung aus den 1930ern im Stadtmuseum (Schenkung 2023) und dass über Fritz Knitter kaum etwas bekannt ist (Adressbucheinträge 1913/14 und 1938/39). Erzählt: dass die vier Frauen sprechen und ausgerechnet über ihren eigenen Zeichner tratschen; der Vergleich mit Zille ist eine gängige Einordnung, kein Urteil Knitters über sich selbst.",

    fakten: [
      "Die Zeichnungen Fritz Knitters entstanden vorwiegend in den 1930er-Jahren, oft auf Verpackungspapier.",
      "2023 kamen die Blätter durch eine Schenkung in die Sammlung des Stadtmuseums Brandenburg.",
      "In den digitalisierten Adressbüchern der Stadt ist Knitter 1913/14 als Beamter in der Vereinstraße und 1938/39 als städtischer Arbeiter in der Roonstraße verzeichnet.",
      "Sein karikaturhafter, sozialkritischer Stil erinnert an den Berliner Zeichner Heinrich Zille (1858–1929).",
      "Über sein Leben ist sonst kaum etwas bekannt; genau dieses Vergessen erzählt das AR-Erlebnis."
    ],
    quellen: [
      "Stadtmuseum Brandenburg an der Havel, Virtueller Rundgang 90: Fritz Knitter",
      "Stadtmuseum Brandenburg, Virtueller Rundgang 82: digitalisierte Adressbücher",
      "museum-digital Brandenburg, Bestand Stadtmuseum"
    ],
    dialog: [
      { frage: "Wer war Fritz Knitter?",
        stichworte: ["knitter", "zeichner", "künstler", "kuenstler"],
        antwort: "Das wüssten wir auch gern genauer! In den Adressbüchern taucht er auf: 1913 als Beamter in der Vereinstraße, 1938 als städtischer Arbeiter in der Roonstraße. Ob es derselbe Mann war und was dazwischen geschah, weiß niemand. Nur seine Zeichnungen sind geblieben.",
        audio: "assets/audio/antworten/knitter_antwort_1.mp3" },
      { frage: "Warum habt ihr auf Verpackungspapier gemalt?",
        stichworte: ["verpackungspapier", "papier", "gemalt", "material"],
        antwort: "Nicht wir, der Knitter! Feines Zeichenpapier konnte er sich wohl nicht leisten. Also nahm er, was da war: braunes Verpackungspapier. Heute macht genau das seine Blätter so besonders.",
        audio: "assets/audio/antworten/knitter_antwort_2.mp3" },
      { frage: "Wie seid ihr ins Museum gekommen?",
        stichworte: ["museum", "schenkung", "sammlung", "gekommen"],
        antwort: "2023, durch eine Schenkung! Jemand hatte die Blätter all die Jahre aufbewahrt. Das Stadtmuseum im Frey-Haus erkannte die Qualität und nahm uns in die Sammlung auf. Seitdem tratschen wir wieder öffentlich.",
        audio: "assets/audio/antworten/knitter_antwort_3.mp3" },
      { frage: "Wer ist dieser Zille?",
        stichworte: ["zille", "berlin", "vergleich", "stil"],
        antwort: "Heinrich Zille, der berühmte Berliner Zeichner der kleinen Leute. Unser Knitter hatte denselben Blick: karikaturhaft, warmherzig und mit einem frechen Spruch unter jedem Bild. Nur berühmt wurde er damit nie.",
        audio: "assets/audio/antworten/knitter_antwort_4.mp3" },
      { frage: "Über wen redet ihr gerade?",
        stichworte: ["über wen", "ueber wen", "redet ihr", "tratscht", "klatsch", "gerede", "wer ist gemeint"],
        antwort: "Über den Mann mit der spitzen Feder natürlich. Der hat hier gesessen und uns gezeichnet, als wären wir nicht da. Fritz Knitter hieß er. Beamter war er zuerst, später städtischer Arbeiter, und gezeichnet hat er trotzdem immer, sogar auf Verpackungspapier, sagt man. Über den reden wir. Und über jeden, der vorbeigeht. Sie zum Beispiel stehen jetzt auch schon eine Weile da.",
        audio: "assets/audio/antworten/knitter_antwort_5.mp3" },
      { frage: "Stört es euch, dass er euch heimlich gezeichnet hat?",
        stichworte: ["heimlich", "gezeichnet", "stört", "stoert", "erlaubnis", "gefragt", "ohne zu fragen"],
        antwort: "Anfangs schon. Man sitzt hier, hält ein Schwätzchen, und der Herr hält die Nase in sein Papier und macht Striche. Gefragt hat er nie. Aber sehen Sie es einmal so: Die Leute vergleichen ihn mit dem Zille aus Berlin, weil er den kleinen Leuten aufs Maul und auf die Hüte geschaut hat. Ihn kennt heute kaum noch jemand. Uns aber hängen sie ins Stadtmuseum. Wer hat da nun den besseren Schnitt gemacht?",
        audio: "assets/audio/antworten/knitter_antwort_6.mp3" }
    ],
    kiHinweis: true
  },

  // ==========================================================================
  // WERK 4: ROLAND VON BRANDENBURG  (Video in Produktion, Seedance 2.0)
  // ==========================================================================
  {
    id: "roland",
    freihandBild: "assets/bilder/freihand_roland.png",  // Freihand-Hintergrund (Outpainting, PNG aus Photoshop; App probiert notfalls .jpg)
    freihandLage: { cx: 0.5, cy: 0.5, breite: 0.85, seite: 2.0372 },  // Hochformat: mittig, 85 % Breite; seite = Hoehe/Breite des Originals
    titel: "Der Roland von Brandenburg",
    untertitel: "Sandsteinfigur von 1474 · Altstädtischer Markt",
    // inProduktion entfernt am 19.07.2026: Test-Fassungen (roh final + idle) sind in der App
    marker: "assets/markers/roland/roland",
    video:  "assets/videos/roland.mp4",
    videoIdle: "assets/videos/roland_idle.mp4",   // Test-Fassung 19.07., stumm komprimiert
    audio:  "assets/audio/roland.mp3",
    bild:   "assets/bilder/roland.jpg",   // Standbild-Fallback (Datei noch ablegen)
    kalibrierung: { position: "0 0 -20", rotation: "-90 0 0", scale: "20 20 20" },

    geschichte: "Habt acht! Ich bin der Roland von Brandenburg, aus Sandstein gehauen anno 1474, und ein hölzerner Vorgänger stand hier schon um 1402. Ich bin kein Denkmal für einen Ritter, ich bin ein Zeichen: für Stadtrecht, Marktrecht und eigene Gerichtsbarkeit. Kurz: für die Freiheit dieser Stadt. 1716 musste ich umziehen, ich stand den Soldaten beim Exerzieren im Weg. Die Kriege habe ich versteckt überstanden, und seit 1946 halte ich Wache vor dem Altstädtischen Rathaus. Auf meinem Kopf wächst übrigens der Donnerbart, eine Hauswurz. Die Legende sagt, sie schütze vor Blitzen. Ich sage: In fünfeinhalb Jahrhunderten hat es hier noch nie eingeschlagen. Man muss nur dran glauben.",

    wahrErzaehlt: "Belegt: entstanden 1474; 1716 vom Neustädtischen Markt vor das Neustädtische Rathaus gerückt (die Figur behinderte die Soldaten beim Exerzieren, genehmigt von König Friedrich Wilhelm I.); 1941 zum Schutz vergraben, 1946 vor dem Altstädtischen Rathaus aufgestellt. Erzählt: der Ritterton und der Ärger über die Tauben.",

    fakten: [
      "Die 5,35 Meter hohe Sandsteinfigur wurde 1474 geschaffen; ein hölzerner Vorgänger ist um 1402 belegt.",
      "Der Roland symbolisiert Marktrecht, eigene Gerichtsbarkeit und die Freiheit der Stadt.",
      "In einer Mulde auf dem Kopf wächst der Donnerbart (Hauswurz), der Legende nach ein Schutz gegen Blitzschlag.",
      "1716 wurde die Figur mit Genehmigung des Soldatenkönigs Friedrich Wilhelm I. versetzt, weil sie beim Exerzieren störte.",
      "1941 zum Schutz vor Bombenangriffen demontiert, überstand der Roland die Zerstörung des Neustädtischen Rathauses 1945 und steht seit 1946 vor dem Altstädtischen Rathaus.",
      "Er gilt als eine der schönsten Rolandfiguren Norddeutschlands."
    ],
    quellen: [
      "Stadt Brandenburg an der Havel: Rathaus und Roland (stadt-brandenburg.de)",
      "museum-digital Brandenburg, Objekt 71092: Roland-Statue von 1474",
      "Wikipedia: Altstädtisches Rathaus (Brandenburg an der Havel)"
    ],
    dialog: [
      { frage: "Wie alt bist du?",
        stichworte: ["alt", "jahre", "1474", "wann"],
        antwort: "1474 wurde ich aus Sandstein gehauen, also weit über 500 Jahre alt. Und mein hölzerner Vorgänger stand hier schon um 1402. Wir Rolande sind Geduldsmenschen.",
        audio: "assets/audio/antworten/roland_antwort_1.mp3" },
      { frage: "Wofür stehst du eigentlich?",
        stichworte: ["wofür", "wofuer", "bedeutung", "symbol", "freiheit", "recht"],
        antwort: "Für die Freiheit dieser Stadt! Marktrecht, eigene Gerichtsbarkeit, Unabhängigkeit. Wo ein Roland steht, regiert die Stadt sich selbst. Deshalb halte ich das Schwert aufrecht: als Zeichen des Rechts.",
        audio: "assets/audio/antworten/roland_antwort_2.mp3" },
      { frage: "Was ist das auf deinem Kopf?",
        stichworte: ["kopf", "donnerbart", "pflanze", "hauswurz"],
        antwort: "Mein Donnerbart! In der Mulde auf meinem Kopf wächst Hauswurz. Die Legende sagt, er schütze mich vor Blitzschlag. Bis heute hat es funktioniert, ich sage nur so viel.",
        audio: "assets/audio/antworten/roland_antwort_3.mp3" },
      { frage: "Wie hast du den Krieg überstanden?",
        stichworte: ["krieg", "bomben", "überstanden", "ueberstanden", "1945", "zerstört", "zerstoert"],
        antwort: "Mit Glück und Voraussicht: 1941 hat man mich abgebaut und eingelagert. Das Neustädtische Rathaus, vor dem ich stand, wurde 1945 zerstört. Ich blieb unversehrt und stehe seit 1946 hier vor dem Altstädtischen Rathaus.",
        audio: "assets/audio/antworten/roland_antwort_4.mp3" },
      { frage: "Warum bist du umgezogen?",
        stichworte: ["umgezogen", "umzug", "1716", "standort", "früher", "frueher"],
        antwort: "1716 war ich den Soldaten beim Exerzieren im Weg! Mit Genehmigung des Soldatenkönigs Friedrich Wilhelm I. versetzte man mich vor das Neustädtische Rathaus. Seit 1946 stehe ich nun hier. Ein Roland beschwert sich nicht.",
        audio: "assets/audio/antworten/roland_antwort_5.mp3" },
      { frage: "Was hast du gegen die Tauben?",
        stichworte: ["tauben", "vögel", "voegel", "taube", "vogel", "dreck"],
        antwort: "Fragen Sie das mal jemanden, der seit über fünfhundert Jahren stillhalten muss. Ich halte das Schwert aufrecht für die Freiheit dieser Stadt, und dann kommt so ein gefiedertes Etwas und landet ausgerechnet da oben, wo mein Donnerbart wächst. In der Mulde auf meinem Kopf, wohlgemerkt, meiner einzigen Grünanlage. Aushalten gehört zum Amt. Gefallen muss es mir nicht.",
        audio: "assets/audio/antworten/roland_antwort_6.mp3" },
      { frage: "Bist du der einzige Roland?",
        stichworte: ["einzige", "andere rolande", "weitere", "bremen", "kollegen", "wo noch", "nur du"],
        antwort: "Keineswegs. In vielen Städten des Nordens steht einer von uns, immer dort, wo eine Stadt auf ihr Marktrecht und ihre Freiheit pochte. Ich stehe seit 1474 hier, fünf Meter fünfunddreißig, und man sagt mir nach, ich sei einer der schönsten von allen. Ich widerspreche dem nicht. Zusammenkommen tun wir freilich nie. Beweglichkeit ist nicht die Stärke unseres Standes.",
        audio: "assets/audio/antworten/roland_antwort_7.mp3" }
    ],
    kiHinweis: true
  },

  // ==========================================================================
  // WERK 5: PLAUER STRASSE UM 1920; FONTANE UND DER WIESIKE-WEIN  (in Produktion)
  // ==========================================================================
  {
    id: "fontane",
    freihandBild: "assets/bilder/freihand_fontane.png",  // Freihand-Hintergrund (Outpainting, PNG aus Photoshop; App probiert notfalls .jpg)
    freihandLage: { cx: 0.5, cy: 0.5, breite: 1.0, seite: 0.7513 },  // Querformat: volle 1080-px-Breite; seite = Hoehe/Breite des Originals
    titel: "Plauer Straße um 1920",
    untertitel: "Theodor Fontane und die Wiesike'sche Weinhandlung",
    // inProduktion entfernt am 19.07.2026: Test-Fassungen (roh final + idle) sind in der App
    marker: "assets/markers/fontane/fontane",
    video:  "assets/videos/fontane.mp4",
    videoIdle: "assets/videos/fontane_idle.mp4",   // Test-Fassung 19.07., stumm komprimiert
    audio:  "assets/audio/fontane.mp3",
    bild:   "assets/bilder/fontane.jpg",   // Standbild-Fallback (Datei noch ablegen)
    kalibrierung: { position: "0 0 -20", rotation: "-90 0 0", scale: "20 20 20" },

    geschichte: "Sehen Sie die Kutschen? Alle haben es eilig. Nur der Wein hat Zeit. Wiesike mein Name, Weinhandlung in der Plauer Straße, seit 1787 in Familienhand. Ganz hinten im Keller lag ein Rheinwein, den ich nie verkauft habe. Zu schade für Kundschaft, ehrlich gesagt. Aber mein Bruder draußen in Plaue hatte einen Gast, einen Dichter aus Berlin, der kam jedes Jahr wieder. Für den habe ich sie hinausgeschickt, Flasche um Flasche. Der Herr Fontane schrieb später, er teile seine Tage dort zwischen Schopenhauer, altem Rheinwein und Naturgenuss. In dieser Reihenfolge, wohlgemerkt. Und wenn er abends am Ufer heimwärts schwankte, sagen die Leute, trug er dem Wasser Gedichte vor. Das steht in keinem Buch. Aber gute Geschichten reifen ja auch im Keller.",

    wahrErzaehlt: "Belegt: die Weinhandlung in der Plauer Straße (seit 1787 in Familienhand), die Brüder Wiesike, Fontanes jährliche Besuche 1874 bis 1880 und sein Wort vom „alten Rheinwein“. Erzählt: die zurückgehaltene Flasche und der schwankende Heimweg.",

    fakten: [
      "Die Weinhandlung in der Plauer Straße 19 (Ecke Huckstraße) kam 1787 durch Einheirat an die Familie Wiesike; zu Fontanes Zeit führte sie Friedrich Wilhelm Wiesike. In der Nacht zum 1. Mai 1945 brannte sie nieder; die alten Gewölbekeller blieben erhalten.",
      "Theodor Fontane (1819–1898) war mit dem Gutsbesitzer Carl Ferdinand Wiesike befreundet und besuchte ihn zwischen 1874 und 1880 wiederholt bei Plaue.",
      "Der Rheinwein, den Wiesike seinen Gästen ausschenkte, stammte aus dem Keller der Handlung in der Plauer Straße; Fontane fuhr auf dem Kutschweg vom Bahnhof daran vorbei.",
      "Fontane war mit den Wiesikes nicht verwandt, nur befreundet; ein oft wiederholter Irrtum.",
      "In Fünf Schlösser (1889) setzte Fontane dem Ort ein literarisches Denkmal: zwischen Schopenhauer, altem Rheinwein und Naturgenuss.",
      "Das Geschäftshaus brannte in der Nacht zum 1. Mai 1945 nieder, nur die Gewölbekeller blieben erhalten; die Fotografie um 1920 zeigt es mit dem Plauer Torturm im Hintergrund."
    ],
    quellen: [
      "Faltkarte Begegne Fontane (2019), Station 17 Plauer Straße",
      "Erlebnis Brandenburg, Fontane-200-Portal: Plauer Straße und Carl Ferdinand Wiesike",
      "Theodor Fontane: Fünf Schlösser (1889), Kapitel zu Plaue",
      "Wikipedia: Theodor Fontane, Schloss Plaue",
      "Märkische Allgemeine Zeitung: Die Weine von Wiesike kamen aus der halben Welt (Alert, 30.01.2023)"
    ],
    dialog: [
      { frage: "Wer sind Sie eigentlich?",
        stichworte: ["wer", "bist", "sind", "sie", "name", "vorstellen", "beruehmt", "berühmt"],
        antwort: "Friedrich Wilhelm Wiesike, Weinhändler. Unser Haus in der Plauer Straße 19, Ecke Huckstraße, führt seit 1787 Wein, und unseren berühmtesten Kunden habe ich hier drinnen vermutlich nie bedient: Sein Wein ging jedes Jahr hinaus nach Plaue, zu meinem Bruder und dessen Gast, dem Herrn Fontane.",
        audio: "assets/audio/antworten/fontane_antwort_1.mp3" },
      { frage: "War Fontane wirklich in diesem Laden?",
        stichworte: ["laden", "wirklich", "drin", "betreten", "gekauft", "fontane"],
        antwort: "Ehrlich gesagt: Belegt ist das nicht. Verbürgt ist, dass er auf dem Kutschweg vom Bahnhof an meinem Laden vorbeifuhr und dass sein Rheinwein aus genau diesem Keller stammte. Die Szene im Laden ist eine erzählerische Verdichtung, das geben wir offen zu.",
        audio: "assets/audio/antworten/fontane_antwort_2.mp3" },
      { frage: "Wer war Carl Ferdinand Wiesike?",
        stichworte: ["wiesike", "carl", "ferdinand", "freund", "bruder"],
        antwort: "Mein Bruder draußen in Plaue: Gutsbesitzer, Verehrer Schopenhauers und der Gastgeber des Herrn Fontane. Zwischen 1874 und 1880 kam der Dichter viele Male; seine Tage dort teilte er, wie er selbst schrieb, zwischen Schopenhauer, altem Rheinwein und Naturgenuss.",
        audio: "assets/audio/antworten/fontane_antwort_3.mp3" },
      { frage: "War Fontane mit euch verwandt?",
        stichworte: ["verwandt", "familie", "onkel", "verwandtschaft"],
        antwort: "Nein, das ist ein hartnäckiger Irrtum, auf den sogar moderne Maschinen hereinfallen! Der Herr Fontane war mit uns Wiesikes nicht verwandt, nur mit meinem Bruder befreundet. Prüfen Sie ruhig die Quellen; in meinem Geschäft zählt auch nur, was im Buch steht.",
        audio: "assets/audio/antworten/fontane_antwort_4.mp3" },
      { frage: "Woher kam der Wein?",
        stichworte: ["wein", "rheinwein", "keller", "flasche", "woher"],
        antwort: "Aus meinem Gewölbekeller, ganz hinten, wo die guten Flaschen liegen. Seit 1787 ist die Handlung in Familienhand, und der beste Rheinwein ging von hier Flasche um Flasche hinaus nach Plaue. Manche Geschichten beginnen eben mit einer Flasche.",
        audio: "assets/audio/antworten/fontane_antwort_5.mp3" },
      { frage: "Was wurde aus dem Haus?",
        stichworte: ["haus", "heute", "geworden", "brand", "1945"],
        antwort: "Das Geschäftshaus in der Plauer Straße 19 brannte in der Nacht zum 1. Mai 1945 nieder, nur die alten Gewölbekeller blieben erhalten. Geblieben ist auch die Fotografie um 1920 mit dem Plauer Torturm, genau das Bild, das hier vor Ihnen hängt.",
        audio: "assets/audio/antworten/fontane_antwort_6.mp3" },
      { frage: "Was ist da eben zerbrochen?",
        stichworte: ["zerbrochen", "kaputt", "runtergefallen", "scherben", "gescheppert", "malheur", "was war das"],
        antwort: "Sie haben es gehört. Eine Flasche, und ausgerechnet eine von den guten. Ich hatte sie gegen das Licht gehalten, so wie man das tut, und dann war der Boden schneller als meine Hand. Kein Wort zu meinem Bruder in Plaue, ja? Der wartet nämlich auf genau die. Ein Trost bleibt: Der Keller ist tief, und es liegt noch mehr davon unten. Aber der Jahrgang, meine Güte, der Jahrgang.",
        audio: "assets/audio/antworten/fontane_antwort_7.mp3" },
      { frage: "Hat Herr Fontane meinen Wein je gelobt?",
        stichworte: ["gelobt", "geschmeckt", "gesagt", "zitat", "geurteilt", "fünf schlösser", "fuenf schloesser"],
        antwort: "Auf seine Art, und aus seiner Feder wiegt das schwer. Überliefert ist, er habe bei meinem Bruder die Stunden zwischen Schopenhauer, altem Rheinwein und Naturgenuss gewissenhaft geteilt. Beachten Sie die Reihenfolge, ich habe sie mir gemerkt. Ein Philosoph vor meinem Wein, damit kann ich leben. Gekommen ist er ja trotzdem jedes Jahr wieder, zwischen 1874 und 1880.",
        audio: "assets/audio/antworten/fontane_antwort_8.mp3" }
    ],
    kiHinweis: true
  },

  // ==========================================================================
  // WERK 6: DAS WACKELAUTO  (Video in Produktion)
  // ==========================================================================
  {
    id: "wackelauto",
    freihandBild: "assets/bilder/freihand_wackelauto.png",  // Freihand-Hintergrund (Outpainting, PNG aus Photoshop; App probiert notfalls .jpg)
    freihandLage: { cx: 0.5, cy: 0.5, breite: 1.0, seite: 0.5835 },  // Querformat: volle 1080-px-Breite; seite = Hoehe/Breite des Originals
    titel: "Das Wackelauto",
    untertitel: "Patentwerk E. P. Lehmann, 1903 · Stadtmuseum Brandenburg",
    // inProduktion entfernt am 19.07.2026: Test-Fassungen (roh final + idle) sind in der App
    marker: "assets/markers/wackelauto/wackelauto",
    video:  "assets/videos/wackelauto.mp4",
    videoIdle: "assets/videos/wackelauto_idle.mp4",   // Test-Fassung 19.07., stumm komprimiert
    audio:  "assets/audio/wackelauto.mp3",
    bild:   "assets/bilder/wackelauto.jpg",   // Standbild-Fallback (Datei noch ablegen)
    kalibrierung: { position: "0 0 -20", rotation: "-90 0 0", scale: "20 20 20" },

    geschichte: "Tut-tut! Steigen Sie ein, ich gebe eine Runde Stadtgeschichte. Gebaut wurde ich 1903 im Patentwerk von Ernst Paul Lehmann, hier in Brandenburg an der Havel. Blech, handbemalt, mit Schwungradantrieb: einmal kräftig kurbeln, und ich wackle los, daher der Name Wackelauto. Meine Brüder und ich waren ein Welterfolg, Lehmanns Blechspielzeug fuhr in Kinderzimmern rund um den Globus, bis nach Amerika. Heute stehe ich im Stadtmuseum, und mein Lack hat ein paar Ehrenkratzer. Aber unter uns: Der Motor läuft noch tadellos. Also, wo darf es hingehen? Und halten Sie sich gut fest. Federung war 1903 noch Ansichtssache.",

    wahrErzaehlt: "Belegt: das Patentwerk Lehmann (gegründet 1881), das Wackelauto um 1903 und der weltweite Export; nach dem Krieg Enteignung und Neuanfang der Familie in Nürnberg. Erzählt: die Fahrer-Schnauze und die Stadtrundfahrt.",

    fakten: [
      "Das Wackelauto ist ein Blechspielzeug des Patentwerks E. P. Lehmann in Brandenburg an der Havel aus dem Jahr 1903 (Produktionsnummer 546).",
      "Angetrieben wird es von einem Schwungrad: einmal kräftig anschieben, dann fährt es wackelnd los.",
      "Am Steuer sitzt ein kleiner Junge im Matrosenanzug, das Blech ist rot, gelb und blau handbemalt.",
      "Die Brandenburger Firma Lehmann belieferte mit ihren Blechspielwaren den Weltmarkt.",
      "Heute gehört das Wackelauto zur Sammlung des Stadtmuseums Brandenburg an der Havel."
    ],
    quellen: [
      "Stadtmuseum Brandenburg an der Havel, Virtueller Rundgang 83: Auto im Karton",
      "museum-digital Brandenburg, Bestand Stadtmuseum",
      "Wikipedia: Ernst Paul Lehmann Patentwerk"
    ],
    dialog: [
      { frage: "Wer hat dich gebaut?",
        stichworte: ["gebaut", "hersteller", "lehmann", "firma", "patentwerk"],
        antwort: "Das Patentwerk E. P. Lehmann, hier in Brandenburg an der Havel! 1903 bin ich vom Band gerollt, Produktionsnummer 546. Patent ist Patent, ob in Deutschland oder der ganzen Welt!",
        audio: "assets/audio/antworten/wackelauto_antwort_1.mp3" },
      { frage: "Wie fährst du ohne Batterie?",
        stichworte: ["batterie", "antrieb", "fährst", "faehrst", "motor", "schwungrad"],
        antwort: "Batterie? Brauche ich nicht! In mir steckt ein Schwungrad. Einmal kräftig anschieben, und schon sause ich wackelnd los. Deshalb heiße ich ja Wackelauto.",
        audio: "assets/audio/antworten/wackelauto_antwort_2.mp3" },
      { frage: "Warst du wirklich weltberühmt?",
        stichworte: ["weltberühmt", "weltberuehmt", "weltmarkt", "export", "verkauft"],
        antwort: "Und ob! Die Blechspielwaren aus Brandenburg gingen in die ganze Welt. Kinder in Amerika, England und anderswo haben mit Autos wie mir gespielt. Brandenburg war damals ein großes Versprechen.",
        audio: "assets/audio/antworten/wackelauto_antwort_3.mp3" },
      { frage: "Wer sitzt da am Steuer?",
        stichworte: ["steuer", "junge", "fahrer", "matrose", "sitzt"],
        antwort: "Mein treuester Passagier: ein kleiner Junge im Matrosenanzug! Seit 1903 hält er meine Lenkkurbel fest. Wir zwei haben noch keine einzige Panne gehabt.",
        audio: "assets/audio/antworten/wackelauto_antwort_4.mp3" },
      { frage: "Warum wackelst du eigentlich so?",
        stichworte: ["wackelst", "wackeln", "wackel", "zittern", "ruckeln", "bewegung", "warum so"],
        antwort: "Das ist kein Wackeln, das ist Fahrgefühl. In mir steckt ein Schwungrad, kein Uhrwerk und kein Motor, und beim Losfahren taumele ich wie ein echtes Automobil über Kopfsteinpflaster. Meinen Namen habe ich genau daher. Ein Auto, das brav geradeaus fährt, hätte 1903 im Kinderzimmer auch niemanden hinter dem Ofen hervorgeholt.",
        audio: "assets/audio/antworten/wackelauto_antwort_5.mp3" },
      { frage: "Warum steigt dein Fahrer aus und schiebt?",
        stichworte: ["schiebt", "schieben", "aussteigen", "steigt aus", "anschieben", "kurbeln", "starten", "springt nicht an"],
        antwort: "Weil das mein Motor ist. Ein Schwungrad, kein Benzin, keine Batterie: einmal kräftig anschieben, dann läuft es von allein. Mein Fahrer, der kleine Herr im Matrosenanzug, ist das seit 1903 gewohnt. Er beschwert sich nie. Und ehrlich gesagt hat er auch keine andere Wahl, er ist aus Blech.",
        audio: "assets/audio/antworten/wackelauto_antwort_6.mp3" }
    ],
    kiHinweis: true
  },

  // ==========================================================================
  // WERK 7: DIE AUSGRAEBERIN VOM HASSELBERG  (Interview-Format, in Produktion)
  // ==========================================================================
  {
    id: "bielefeld",
    freihandBild: "assets/bilder/freihand_bielefeld.png",  // Freihand-Hintergrund (Outpainting, PNG aus Photoshop; App probiert notfalls .jpg)
    freihandLage: { cx: 0.5, cy: 0.5, breite: 0.85, seite: 1.5681 },  // Hochformat: mittig, 85 % Breite; seite = Hoehe/Breite des Originals
    titel: "Die Ausgräberin vom Hasselberg",
    untertitel: "Minna Marie Bielefeld bei der Grabung, 1915 · Stadtmuseum Brandenburg",
    // inProduktion entfernt am 19.07.2026: Test-Fassungen (roh final + idle) sind in der App
    marker: "assets/markers/bielefeld/bielefeld",
    video:  "assets/videos/bielefeld.mp4",
    videoIdle: "assets/videos/bielefeld_idle.mp4",   // Test-Fassung 19.07., stumm komprimiert
    audio:  "assets/audio/bielefeld.mp3",
    bild:   "assets/bilder/bielefeld.jpg",
    kalibrierung: { position: "0 0 -20", rotation: "-90 0 0", scale: "20 20 20" },

    geschichte: "Guten Tag, verehrte Hörerinnen und Hörer, wir melden uns vom Hasselberg bei Butzow, im Jahre 1915. Vor mir arbeitet Frau Minna Marie Auguste Bielefeld, und sie gräbt, während wir sprechen, seelenruhig weiter: Urnen, sechzehnhundert Jahre alt. Die Herren der Wissenschaft nennen sie die berüchtigte Frau Oberpostsekretär; sie selbst nimmt das, wie sie mir eben zuruft, als Kompliment. Unterstützt wird sie von ihren Töchtern: Lucie schippt, Herta zeichnet die Funde, an die achthundert Blätter sollen es schon sein. Auf meine Frage, ob das eine Arbeit für Frauen sei, kommt die Antwort ohne Zögern: „Wat der Mann kann, kann ick lange.“ Dem ist, meine Damen und Herren, nichts hinzuzufügen. Nur der Maulwurf dort drüben scheint anderer Meinung. Wir geben zurück ins Studio.",

    wahrErzaehlt: "Belegt: Marie Bielefeld grub ab vor 1914 bis um 1930 am Hasselberg Urnen aus, das Pfarrer-Zitat von 1925, die über 800 Zeichnungen der Töchter, die übervolle Wohnung. Erzählt: der Reporter (1915 gab es keine Ton-Interviews), der Maulwurf und die Suppenterrine.",

    fakten: [
      "Aus dem Notizbuch des Reporters: Minna Marie Auguste Bielefeld (1866–1947) gräbt ab der Zeit vor dem Ersten Weltkrieg bis um 1930 am Hasselberg bei Butzow völkerwanderungszeitliche Urnengräber aus (3.–5. Jahrhundert). Habe mich vor Ort überzeugt: Sie weiß genau, was sie tut.",
      "Notiert: Pfarrer Holtze nannte sie 1925 verärgert „die durch ihre Buddeleien berüchtigte Frau Oberpostsekretär Bielefeld“. Die Dame trägt den Titel mit sichtbarem Vergnügen.",
      "Am Rande der Grabung beobachtet: Tochter Lucie (1891–1962) schaufelt, Tochter Herta (1893–1975) zeichnet; über 800 Fundzeichnungen, rund 400 davon liegen heute im Stadtmuseum. Ein eingespieltes Trio.",
      "Beim Hausbesuch in der Jahnstraße 11 notiert: Die Wohnung steht voller Fundgefäße, fein säuberlich in einem Fotoalbum dokumentiert. Man stolpert förmlich über die Völkerwanderung.",
      "Später recherchiert: 1943 verkauften die Frauen 195 Urnen und etwa 80 Beigaben an das Heimatmuseum Köthen; 1965 kehrte die Sammlung nach Brandenburg zurück.",
      "Nachtrag der Redaktion: Die Fundkartei der „Sammlung Bielefeld“ wurde erst kürzlich im Nachlass Herta Bielefelds wiederentdeckt (Stadtmuseum, Rundgang 86). Die Geschichte gräbt eben nach."
    ],
    quellen: [
      "Stadtmuseum Brandenburg an der Havel, Digitales Stadtmuseum, Virtueller Rundgang 86 (Autorin: Anja Grothe)",
      "Eigene Fundkontext-Notiz bielefeld_02 (zusammengefasst aus Stadtmuseum, Rundgang 86; ein eigener Wikipedia-Artikel zu Butzow existiert nicht)"
    ],
    dialog: [
      { frage: "Frau Bielefeld, was tun Sie da eigentlich?",
        stichworte: ["machen", "buddeln", "graben", "grabung"],
        antwort: "Buddeln, sagt der Volksmund. Ich rette Urnen, sechzehnhundert Jahre alt, bevor die Sandgrube sie frisst. Die Herren vom Historischen Verein schnauben dazu. Sollen sie.",
        audio: "assets/audio/antworten/bielefeld_antwort_1.mp3" },
      { frage: "Frau Bielefeld, wer hilft Ihnen bei der Arbeit?",
        stichworte: ["hilft", "töchter", "toechter", "familie", "lucie", "herta"],
        antwort: "Meine Töchter. Lucie schaufelt, Herta zeichnet. Über achthundert Blätter haben die beiden gefertigt, jede Scherbe einzeln. Ohne Dokumentation ist Graben nur Wühlen.",
        audio: "assets/audio/antworten/bielefeld_antwort_2.mp3" },
      { frage: "Man nennt Sie berüchtigt. Wie kommt das?",
        stichworte: ["berüchtigt", "beruechtigt", "pfarrer", "ruf"],
        antwort: "Der Herr Pfarrer Holtze schrieb 1925 ins Vereinsbuch, die Tongefäße habe sich „die durch ihre Buddeleien berüchtigte Frau Oberpostsekretär Bielefeld geholt“. Ich nehme es als Kompliment.",
        audio: "assets/audio/antworten/bielefeld_antwort_3.mp3" },
      { frage: "Was wurde eigentlich aus Ihrer Sammlung?",
        stichworte: ["sammlung", "geworden", "köthen", "koethen", "verkauft"],
        antwort: "1943 gingen 195 Urnen nach Köthen, die Zeiten waren schwer. 1965 kam die Sammlung zurück nach Brandenburg. Heute liegt sie im Stadtmuseum, samt unserer Kartei, die man erst kürzlich wiederfand.",
        audio: "assets/audio/antworten/bielefeld_antwort_4.mp3" },
      { frage: "Und was war nun mit dem Maulwurf?",
        stichworte: ["maulwurf", "konkurrenz", "tier"],
        antwort: "Ach, der. Kam mir heute früh mitten in die Grabung. Gräbt schneller als ich, das gebe ich zu. Aber er dokumentiert nichts, und damit ist er raus aus der Wissenschaft. Kleiner Scherz übrigens, den Maulwurf habe ich erfunden. Fast alles andere nicht.",
        audio: "assets/audio/antworten/bielefeld_antwort_5.mp3" },
      { frage: "Warum haben Ihre Töchter alles gezeichnet?",
        stichworte: ["gezeichnet", "zeichnungen", "zeichnen", "dokumentiert", "achthundert"],
        antwort: "Weil ein Fund, den niemand festhält, verloren ist. Fotografiert haben wir auch, die Gefäße stehen fein säuberlich in einem Album. Aber eine Aufnahme zeigt nicht, wie eine Scherbe gebrochen ist und wie die Stücke im Boden lagen. Dafür braucht es den Stift. Über achthundert Blätter sind so entstanden, rund vierhundert davon liegen heute im Stadtmuseum. Ohne sie wüsste man von meiner Arbeit so gut wie nichts.",
        audio: "assets/audio/antworten/bielefeld_antwort_6.mp3" }
    ],
    kiHinweis: true
  },
];
