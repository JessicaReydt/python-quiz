# 🐍 Python Lern-Quiz

Ein kleines, interaktives Quiz, das grundlegende Python-Konzepte abfragt – entstanden aus meinem eigenen Lernprozess.



## Idee & Hintergrund

Während ich für meine Umschulung zur Fachinformatikerin Anwendungsentwicklung Python gelernt habe, habe ich gemerkt, dass reines, „trockenes“ Lernen auf Dauer anstrengend wird.  
Um etwas Abwechslung zu haben und das Gelernte aktiver zu wiederholen, wollte ich ein eigenes Projekt bauen – und so ist dieses **Python Lern-Quiz** entstanden.

Ziele des Projekts:

- Python-Grundlagen (Variablen, Datentypen, Schleifen, Funktionen usw.) spielerisch wiederholen.
- Ein **sauber strukturiertes Python-Projekt** aufbauen (Trennung von Logik und UI).
- Das Quiz sowohl als **Konsolenanwendung** als auch als kleine **Desktop-App (Flet-GUI)** nutzbar machen.
- Eine **EXE-Datei** bereitstellen, die ohne Python-Installation getestet werden kann.




## Features

- 35 Multiple-Choice-Fragen zu grundlegenden Python-Konzepten.
- Auswertung mit Punktzahl und prozentualem Ergebnis.
- Unterschiedliche Feedback-Texte je nach Ergebnis (inkl. Emojis).
- Zwei Oberflächen:
  - **Konsole (CLI)** – Python pur.
  - **Flet-GUI** – moderne Oberfläche mit Dark Mode, Buttons und Fortschrittsbalken.
- Saubere Trennung von:
  - **Daten** (`data.py`)
  - **Kernlogik** (`core.py`)
  - **Benutzeroberflächen** (`console_app.py`, `flet_app.py`)




## Projektstruktur

```text
python-quiz/
├── build/
│ └── PythonQuiz/ # Build-Artefakte von PyInstaller (Zwischendateien)
├── dist/
│ └── PythonQuiz.exe # fertige Windows-EXE (GUI-Version)
├── quiz/
│ ├── pycache/ # von Python erzeugte Cache-Dateien
│ ├── init.py # macht 'quiz' zum Python-Paket
│ ├── console_app.py # Konsolen-Oberfläche
│ ├── core.py # QuizEngine (Kernlogik)
│ ├── data.py # Fragen & Antworten (QUESTIONS)
│ └── flet_app.py # Flet-GUI
├── PythonQuiz.spec # PyInstaller-Konfiguration
├── README.md # diese Datei
└── requirements.txt # Python-Abhängigkeiten (z.B. flet)

```


## 1. Nutzung als Konsolen-Quiz (Python)

Voraussetzung:  
- Python ist installiert (z.B. 3.13.x).

### 1.1. Projektordner im Terminal öffnen

### 1.2. Konsolen-Quiz starten
- Im Terminal eingeben: python -m quiz.console_app



- Es erscheint ein Text-Menü im Terminal.
- Die Fragen werden nacheinander angezeigt.
- Antworten werden mit `A`, `B` oder `C` eingegeben.
- Am Ende gibt es eine Auswertung mit Kommentar zum Ergebnis.




## 2. Nutzung als GUI-Quiz (Python + Flet)

Voraussetzungen:  
- Python ist installiert.  
- Flet ist installiert (einmalig im Terminal): pip install flet

### 2.1. GUI-Quiz starten

Im Projektordner: 
- im Terminal eingeben: python -m quiz.flet_app


- Es öffnet sich ein Fenster mit:
  - Titel „🐍 Python Lern-Quiz“
  - Startbildschirm mit Button „🚀 Quiz starten“
  - Dark-Mode-Design, Fortschrittsbalken, visuelles Feedback pro Frage und Ergebnisanzeige.




## 3. Nutzung als fertige Windows-App (EXE)

Für Tester ohne Python-Installation gibt es eine fertige **EXE-Datei**, die mit PyInstaller aus der Flet-Version gebaut wurde.
[👉 PythonQuiz.exe herunterladen](https://github.com/JessicaReydt/python-quiz/releases/latest)


### 3.1. Aufbau der EXE

Die EXE wurde mit folgendem Befehl erzeugt:

pyinstaller --onefile --windowed --name "PythonQuiz" quiz\flet_app.py

- `--onefile` → eine einzelne EXE-Datei  
- `--windowed` → kein zusätzliches Konsolenfenster  
- `--name "PythonQuiz"` → Name der Ausgabedatei

Ergebnis:

dist/PythonQuiz.exe

### 3.2. Start der EXE

1. `PythonQuiz.exe` (z.B. aus dem Ordner `dist` oder einem bereitgestellten Download) auf einen Windows-Rechner kopieren.  
2. **Doppelklick auf `PythonQuiz.exe`**  
3. Die Flet-GUI des Quiz startet direkt – **ohne**, dass Python oder Flet installiert sein müssen.

Damit ist das Testen sehr einfach:
- Entweder per **Doppelklick auf die EXE**,
- oder – für Entwickler – direkt aus dem Python-Code heraus.




## Technische Highlights

- **Trennung von Logik und Darstellung**  
  - `QuizEngine` in `core.py` enthält die komplette Kernlogik (Fragenwechsel, Auswertung, Prozentberechnung).  
  - Die Konsolen-Version und die Flet-GUI nutzen beide dieselbe Engine.

- **Wiederverwendbare Datenbasis**  
  - Alle Fragen liegen zentral in `data.py` in der Liste `QUESTIONS`.  
  - Änderungen an den Fragen wirken sich sofort in beiden UIs (Konsole + GUI) aus.

- **Zwei Frontends auf gleicher Basis**  
  - CLI-Frontend: Fokus auf Python-Ein-/Ausgabe (`input`, `print`).  
  - GUI-Frontend: Flet, modernes Design, Fortschrittsbalken, visuelles Feedback.

- **Verteilung als Standalone-EXE**  
  - Mit PyInstaller als Einzeldatei (`--onefile`, `--windowed`).  
  - Kein Setup, keine Python-Installation notwendig.

## Warum dieses Projekt in meinem Portfolio ist

Dieses Quiz ist eines meiner ersten eigenständigen Python-Projekte, bei dem ich:

- ein eigenes Lernproblem (trockene Theorie) in eine praktische Lösung übersetzt habe,
- eine **modulare Python-Struktur** umgesetzt habe,
- zwei verschiedene Oberflächen auf derselben Kernlogik aufbauen konnte,
- und den Schritt zur **packaged Desktop-Anwendung (EXE)** gegangen bin.

Es zeigt, wie ich an Probleme herangehe:
- erst **fachliches Ziel** (Lernen & Wiederholen),
- dann **saubere Struktur** (Core, Daten, UI),

- dann **Benutzerfreundlichkeit** (GUI und EXE für einfache Tests).

