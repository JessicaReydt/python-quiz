import flet as ft       # Flet-Bibliothek importieren, um die App-Oberfläche zu erstellen
import threading        # Import für Threads, damit ich kurze Pausen ohne die App zu blockieren einbauen kann
import time             # Import für Zeitfunktionen, z.B. sleep
import asyncio          # Import für asynchrone Funktionen (wird von Flet intern benötigt)

#  Fragen-Array für das Quiz

quiz = [

    # 1–10
    {"question": "Was ist eine Variable?", 
     "options": ["A) Eine Funktion, die Code wiederholt", "B) Ein Speicherplatz für einen Wert", "C) Ein spezieller Datentyp für Zahlen"], 
     "answer": "B"},

    {"question": "Was bedeutet 'definieren'?", 
     "options": ["A) Etwas festlegen oder beschreiben", "B) Eine Schleife ausführen", "C) Einen Wert löschen"], 
     "answer": "A"},

    {"question": "Was bedeutet 'deklarieren'?", 
     "options": ["A) Eine Variable bekannt machen", "B) Eine Liste erstellen", "C) Eine Funktion beenden"], 
     "answer": "A"},

    {"question": "Was ist ein String?", 
     "options": ["A) Eine Zahl mit Nachkommastellen", "B) Eine Sammlung von Wahrheitswerten", "C) Eine Zeichenkette aus Text"], 
     "answer": "C"},

    {"question": "Was ist ein Float?", 
     "options": ["A) Eine ganze Zahl", "B) Eine Fließkommazahl", "C) Ein logischer Wert"], 
     "answer": "B"},

    {"question": "Was ist ein Integer?", 
     "options": ["A) Eine Liste aus Zahlen", "B) Eine ganze Zahl", "C) Eine Textvariable"], 
     "answer": "B"},

    {"question": "Was ist ein Boolean (bool)?", 
     "options": ["A) Ein Wahrheitswert (True/False)", "B) Eine Zahl mit Komma", "C) Eine Schleifenart"], 
     "answer": "A"},

    {"question": "Was sind Listen?", 
     "options": ["A) Eine feste Anzahl an Werten", "B) Eine Sammlung mehrerer Werte in Reihenfolge", "C) Eine Funktion zum Vergleichen"], 
     "answer": "B"},

    {"question": "Was bedeutet 'iterieren'?", 
     "options": ["A) Durch Daten Schritt für Schritt gehen", "B) Einen Datentyp umwandeln", "C) Eine Bedingung prüfen"], 
     "answer": "A"},

    {"question": "Was ist eine while-Schleife?", 
     "options": ["A) Wiederholt Code, solange eine Bedingung wahr ist", "B) Führt Code nur einmal aus", "C) Wiederholt Code für jedes Element einer Liste"], 
     "answer": "A"},


     # 11–20
    {"question": "Was ist eine for-Schleife?", 
     "options": ["A) Wiederholt Code für jedes Element einer Sequenz", "B) Prüft eine Bedingung einmalig", "C) Wird nur mit Zahlen verwendet"], 
     "answer": "A"},

    {"question": "Was ist ein Tupel?", 
     "options": ["A) Eine veränderbare Liste", "B) Eine unveränderbare Liste", "C) Eine Zahl mit Nachkommastellen"], 
     "answer": "B"},

    {"question": "Was ist der Unterschied zwischen while- und for-Schleife?", 
     "options": ["A) while ist bedingungsgesteuert, for läuft über Elemente", "B) Beide sind identisch", "C) for braucht keine Einrückung"], 
     "answer": "A"},

    {"question": "Was sind Dictionaries?", 
     "options": ["A) Listen mit Zahlen", "B) Sammlungen von Schlüssel-Wert-Paaren", "C) Eine Schleifenart"], 
     "answer": "B"},

    {"question": "Was sind Funktionen?", 
     "options": ["A) Codeblöcke, die man wiederverwenden kann", "B) Zufällige Codeabschnitte", "C) Eine spezielle Datentyp-Umwandlung"], 
     "answer": "A"},

    {"question": "Was sind Operatoren?", 
     "options": ["A) Nur Textzeichen", "B) Symbole für Berechnungen oder Vergleiche", "C) Spezielle Datentypen"], 
     "answer": "B"},

    {"question": "Was sind Bedingungen (if)?", 
     "options": ["A) Prüfen, ob etwas wahr ist", "B) Wiederholen Code", "C) Speichern Werte"], 
     "answer": "A"},

    {"question": "Was ist None?", 
     "options": ["A) Ein leerer Wert oder 'nichts'", "B) Eine Funktion", "C) Eine Schleife"], 
     "answer": "A"},

    {"question": "Was ist der Unterschied zwischen '=' und '=='?", 
     "options": ["A) '=' weist zu, '==' vergleicht", "B) Beide sind gleich", "C) '=' vergleicht Zahlen"], 
     "answer": "A"},

    {"question": "Was bedeutet 'Datentyp'?", 
     "options": ["A) Art eines gespeicherten Werts", "B) Ein Kommentar", "C) Eine Variable"], 
     "answer": "A"},


    # 21–30
    {"question": "Was ist eine Schleifenvariable?", 
     "options": ["A) Eine globale Variable", "B) Eine Variable, die sich in einer Schleife ändert", "C) Eine Bedingung"], 
     "answer": "B"},

    {"question": "Was ist ein Index?", 
     "options": ["A) Ein anderer Name für eine Funktion", "B) Die Position eines Elements (ab 0)", "C) Eine Textvariable"], 
     "answer": "B"},

    {"question": "Was bedeutet 'Slicing'?", 
     "options": ["A) Einen Teil einer Liste oder Zeichenkette ausschneiden", "B) Eine Schleife abbrechen", "C) Eine Variable löschen"], 
     "answer": "A"},

    {"question": "Was ist eine Range?", 
     "options": ["A) Eine Liste mit Text", "B) Eine Zahlenfolge", "C) Eine Funktion, die Strings vergleicht"], 
     "answer": "B"},

    {"question": "Was ist eine Bedingungskombination?", 
     "options": ["A) Eine Schleife im if-Block", "B) Verbindung mehrerer Bedingungen mit and/or/not", "C) Ein anderer Name für eine Funktion"], 
     "answer": "B"},

    {"question": "Was sind Kommentare?", 
     "options": ["A) Notizen im Code, die Python ignoriert", "B) Funktionen mit Textausgabe", "C) Variablen für Text"], 
     "answer": "A"},

    {"question": "Was sind Module?", 
     "options": ["A) Schleifenvariablen", "B) Nur Zahlenlisten", "C) Externe oder eigene Python-Dateien mit Code"], 
     "answer": "C"},

    {"question": "Was ist eine Klasse?", 
     "options": ["A) Eine einfache Funktion", "B) Eine Vorlage (Bauplan) für Objekte", "C) Eine Liste von Variablen"], 
     "answer": "B"},

    {"question": "Was sind Objekte?", 
     "options": ["A) Konkrete Instanzen einer Klasse", "B) Nur Datentypen", "C) Textketten"], 
     "answer": "A"},

    {"question": "Was sind Parameter und Argumente?", 
     "options": ["A) Platzhalter in Funktionen und die übergebenen Werte", "B) Nur Kommentare", "C) Logische Operatoren"], 
     "answer": "A"},


    # 31–35
    {"question": "Was ist der Unterschied zwischen lokal und global?", 
     "options": ["A) Global: nur in Schleifen gültig", "B) Lokal: nur in Funktion gültig, global: im ganzen Programm", "C) Lokal: kann überall verwendet werden"], 
     "answer": "B"},

    {"question": "Was ist eine Exception (Fehlerbehandlung)?", 
     "options": ["A) Ein Fehler, der abgefangen werden kann", "B) Eine Art Schleife", "C) Eine Textvariable"], 
     "answer": "A"},

    {"question": "Was ist eine verschachtelte Liste?", 
     "options": ["A) Eine Liste, die andere Listen enthält", "B) Eine Liste aus Zahlen", "C) Eine Liste aus Strings"], 
     "answer": "A"},

    {"question": "Was macht len()?", 
     "options": ["A) Gibt die Länge einer Liste oder Zeichenkette zurück", "B) Löscht eine Variable", "C) Wandelt Text in Zahlen um"], 
     "answer": "A"},

    {"question": "Was macht input()?", 
     "options": ["A) Fragt Benutzereingaben ab", "B) Gibt Zufallszahlen zurück", "C) Beendet das Programm"], 
     "answer": "A"}
     
]


#  Hauptfunktion der App


def main(page: ft.Page):   # page ist das Fenster der App
    
    # Fenster & App Settings

    page.window_width = 400      # Breite des App-Fensters
    page.window_height = 700       # Höhe des App-Fensters
    page.window_resizable = False   # Fenster soll nicht vergrößerbar sein
    page.title = "🐍 Python Quiz"      
    page.bgcolor = ft.Colors.BLACK      # Hintergrundfarbe der App
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER   # Inhalte horizontal zentrieren
    page.vertical_alignment = ft.MainAxisAlignment.CENTER      # Inhalte vertikal zentrieren

    accent = ft.Colors.CYAN_ACCENT_400      # Akzentfarbe für Buttons & Überschriften
    text_color = ft.Colors.WHITE            # Standardfarbe für Text

    current = 0     # Variable für die aktuelle Frage
    score = 0       # Variable für die Anzahl richtiger Antworten


    # UI Elemente

    title = ft.Text("🐍 Python Lern-Quiz", size=28, weight="bold", color=accent)    # Überschrift
    question_text = ft.Text(size=20, color=text_color)      # Textfeld für Frage
    feedback = ft.Text(size=18, color=text_color)           # Textfeld für Feedback nach Antwort
    progress_bar = ft.ProgressBar(width=350, value=0, color=accent)    # Fortschrittsbalken
    progress_text = ft.Text(size=16, color=ft.Colors.WHITE70)        # Text für Fortschritt (Frage X von Y)
    option_buttons = ft.Column(spacing=10, alignment="center")       # Container für Antwort-Buttons

    
    # Startscreen
    
    def start_screen(e=None):       # e=None damit auch ohne Klick aufgerufen werden kann
        page.clean()                # Alle aktuellen Inhalte löschen

        start_btn = ft.ElevatedButton(
            "🚀 Quiz starten",     # Text auf dem Button
            on_click=start_quiz,    # Klick-Event startet das Quiz
            width=250,
            height=50,
            bgcolor=accent,         # Buttonfarbe
            color="black",          # Textfarbe
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=12),     # Abgerundete Ecken
                elevation=5         # Schatten unter dem Button
            )
        )

        start_container = ft.Container(
            content=ft.Column(
                [
                    title,      # Überschrift
                    ft.Text("Teste dein Python-Wissen!", color=text_color, size=18),     # Untertitel
                    start_btn   # Start-Button
                ],
                spacing=20,     # Abstand zwischen Elementen
                alignment=ft.MainAxisAlignment.CENTER,      # Vertikale Ausrichtung
                horizontal_alignment=ft.CrossAxisAlignment.CENTER       # Horizontale Ausrichtung
            ),
            width=350,
            height=600,
            bgcolor=ft.Colors.BLUE_GREY_900,    # Hintergrundfarbe des Containers
            border_radius=20,                   # Abgerundete Ecken
            padding=20,                         # Innenabstand
            alignment=ft.alignment.center       # Inhalt zentrieren
        )

        page.add(start_container)      # Container zur Seite hinzufügen

   
    # Quiz starten
    
    def start_quiz(e):
        nonlocal current, score         # Zugriff auf Variablen außerhalb der Funktion
        current = 0
        score = 0
        page.clean()                    # Alte Inhalte löschen
        page.add(
            ft.Container(
                content=ft.Column(
                    [title, progress_bar, progress_text, question_text, option_buttons, feedback],
                    spacing=15,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                width=350,
                height=600,
                bgcolor=ft.Colors.BLUE_GREY_900,
                border_radius=20,
                padding=20,
                alignment=ft.alignment.top_center
            )
        )
        show_question()                 # Erste Frage anzeigen

    
    # Frage anzeigen
 
    def show_question():
        nonlocal current
        option_buttons.controls.clear()       # Alte Buttons löschen

        if current < len(quiz):               # Prüfen, ob es noch Fragen gibt
            q = quiz[current]                 # Aktuelle Frage
            question_text.value = f"{current + 1}. {q['question']}"      # Frage-Text setzen
            progress_text.value = f"Frage {current + 1} von {len(quiz)}"    # Fortschritt-Text setzen


    # Buttons für Antwortmöglichkeiten erstellen

            for option in q["options"]:
                btn = ft.ElevatedButton(
                    text=option,
                    width=300,
                    height=45,
                    bgcolor=ft.Colors.BLUE_GREY_800,
                    color=ft.Colors.WHITE,
                    style=ft.ButtonStyle(elevation=3, shape=ft.RoundedRectangleBorder(radius=10)),
                    on_click=lambda e, opt=option: check_answer(opt)    # Klick-Event
                )
                option_buttons.controls.append(btn)     # Button zum Container hinzufügen

            progress_bar.value = current / len(quiz)    # Fortschrittsbalken aktualisieren
            feedback.value = ""     # Feedback leeren
            page.update()       # UI aktualisieren
        else:
            show_result()       # Quiz fertig -> Ergebnis anzeigen

   
    # Antwort prüfen
   
    def check_answer(selected_option):
        nonlocal current, score
        correct = quiz[current]["answer"]       # Richtige Antwort

        if selected_option.strip()[0].upper() == correct.upper():       # Prüfen, ob Anfangsbuchstabe der Antwort stimmt
            feedback.value = "✅ Richtig!"      # Feedback-Text
            feedback.color = ft.Colors.GREEN_ACCENT_400
            score += 1      # Punktzahl erhöhen
        else:
            correct_text = next((opt for opt in quiz[current]["options"] if opt.strip().startswith(correct)), correct)      # Richtige Antwort als Text
            feedback.value = f"❌ Falsch! Richtige Antwort: {correct} — {correct_text}"
            feedback.color = ft.Colors.RED_ACCENT_400

        page.update()     # UI aktualisieren


    # Kurze Pause bevor zur nächsten Frage

        def delayed_continue():
            time.sleep(0.8)     # 0.8 Sekunden warten
            continue_quiz()     # Nächste Frage zeigen

        threading.Thread(target=delayed_continue, daemon=True).start()      # Thread starten, damit UI nicht blockiert wird

   
    # Nächste Frage
  
    def continue_quiz():
        nonlocal current
        current += 1        # Frage-Zähler erhöhen
        show_question()     # nächste Frage anzeigen

    
    # Ergebnisanzeige
   
    def show_result():
        page.clean()        # Alte Inhalte löschen
        percent = score / len(quiz)     # Prozentsatz der richtigen Antworten

    # Nachricht & Farbe je nach Ergebnis

        if percent == 1:
            msg, emoji, color = "Perfekt! Du bist ein echter Python-Profi!", "🏆", ft.Colors.GREEN_ACCENT_400
        elif percent >= 0.7:
            msg, emoji, color = "Sehr gut! Du hast Python schon gut verstanden.", "👏", ft.Colors.LIGHT_GREEN_ACCENT_400
        elif percent >= 0.4:
            msg, emoji, color = "Ganz ordentlich, aber etwas Übung schadet nicht.", "🙂", ft.Colors.AMBER_ACCENT_200
        else:
            msg, emoji, color = "Noch etwas lernen – du schaffst das!", "🤔", ft.Colors.RED_ACCENT_200

    # Ergebnis-Text
        result_text = ft.Text(
            f"{emoji} {msg}\nDu hast {score} von {len(quiz)} richtig.",
            size=22,
            color=color,
            weight="bold",
            text_align="center"
    )

    # Restart-Button
        restart_btn = ft.ElevatedButton(
            "🔁 Nochmal spielen",
            on_click=start_screen,      # Klick -> Startscreen
            width=250,
            height=50,
            bgcolor=accent,
            color="black",
            style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            elevation=5,
            overlay_color=ft.Colors.CYAN_200        # Farbe beim Drüberhovern
        )
    )

    # Container mit allen Elementen
        result_container = ft.Container(
            content=ft.Column(
                [title, result_text, restart_btn],      # Überschrift, Ergebnis, Button
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
            width=350,
            height=600,
            bgcolor=ft.Colors.BLUE_GREY_900,
            border_radius=20,
            padding=20,
            alignment=ft.alignment.center
    )

        page.add(result_container)       # Container zur Seite hinzufügen

  
    # App starten
    
    start_screen()      # Startbildschirm anzeigen


if __name__ == "__main__":
    ft.app(target=main)     # App starten
