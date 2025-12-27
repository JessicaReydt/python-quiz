# quiz/data.py
from __future__ import annotations

QUESTIONS = [
    # 1–10
    {
        "question": "Was ist eine Variable?",
        "options": [
            "A) Eine Funktion, die Code wiederholt",
            "B) Ein Speicherplatz für einen Wert",
            "C) Ein spezieller Datentyp für Zahlen",
        ],
        "answer": "B",
    },
    {
        "question": "Was bedeutet 'definieren'?",
        "options": [
            "A) Etwas festlegen oder beschreiben",
            "B) Eine Schleife ausführen",
            "C) Einen Wert löschen",
        ],
        "answer": "A",
    },
    {
        "question": "Was bedeutet 'deklarieren'?",
        "options": [
            "A) Eine Variable bekannt machen",
            "B) Eine Liste erstellen",
            "C) Eine Funktion beenden",
        ],
        "answer": "A",
    },
    {
        "question": "Was ist ein String?",
        "options": [
            "A) Eine Zahl mit Nachkommastellen",
            "B) Eine Sammlung von Wahrheitswerten",
            "C) Eine Zeichenkette aus Text",
        ],
        "answer": "C",
    },
    {
        "question": "Was ist ein Float?",
        "options": [
            "A) Eine ganze Zahl",
            "B) Eine Fließkommazahl",
            "C) Ein logischer Wert",
        ],
        "answer": "B",
    },
    {
        "question": "Was ist ein Integer?",
        "options": [
            "A) Eine Liste aus Zahlen",
            "B) Eine ganze Zahl",
            "C) Eine Textvariable",
        ],
        "answer": "B",
    },
    {
        "question": "Was ist ein Boolean (bool)?",
        "options": [
            "A) Ein Wahrheitswert (True/False)",
            "B) Eine Zahl mit Komma",
            "C) Eine Schleifenart",
        ],
        "answer": "A",
    },
    {
        "question": "Was sind Listen?",
        "options": [
            "A) Eine feste Anzahl an Werten",
            "B) Eine Sammlung mehrerer Werte in Reihenfolge",
            "C) Eine Funktion zum Vergleichen",
        ],
        "answer": "B",
    },
    {
        "question": "Was bedeutet 'iterieren'?",
        "options": [
            "A) Durch Daten Schritt für Schritt gehen",
            "B) Einen Datentyp umwandeln",
            "C) Eine Bedingung prüfen",
        ],
        "answer": "A",
    },
    {
        "question": "Was ist eine while-Schleife?",
        "options": [
            "A) Wiederholt Code, solange eine Bedingung wahr ist",
            "B) Führt Code nur einmal aus",
            "C) Wiederholt Code für jedes Element einer Liste",
        ],
        "answer": "A",
    },

    # 11–20
    {
        "question": "Was ist eine for-Schleife?",
        "options": [
            "A) Wiederholt Code für jedes Element einer Sequenz",
            "B) Prüft eine Bedingung einmalig",
            "C) Wird nur mit Zahlen verwendet",
        ],
        "answer": "A",
    },
    {
        "question": "Was ist ein Tupel?",
        "options": [
            "A) Eine veränderbare Liste",
            "B) Eine unveränderbare Liste",
            "C) Eine Zahl mit Nachkommastellen",
        ],
        "answer": "B",
    },
    {
        "question": "Was ist der Unterschied zwischen while- und for-Schleife?",
        "options": [
            "A) while ist bedingungsgesteuert, for läuft über Elemente",
            "B) Beide sind identisch",
            "C) for braucht keine Einrückung",
        ],
        "answer": "A",
    },
    {
        "question": "Was sind Dictionaries?",
        "options": [
            "A) Listen mit Zahlen",
            "B) Sammlungen von Schlüssel-Wert-Paaren",
            "C) Eine Schleifenart",
        ],
        "answer": "B",
    },
    {
        "question": "Was sind Funktionen?",
        "options": [
            "A) Codeblöcke, die man wiederverwenden kann",
            "B) Zufällige Codeabschnitte",
            "C) Eine spezielle Datentyp-Umwandlung",
        ],
        "answer": "A",
    },
    {
        "question": "Was sind Operatoren?",
        "options": [
            "A) Nur Textzeichen",
            "B) Symbole für Berechnungen oder Vergleiche",
            "C) Spezielle Datentypen",
        ],
        "answer": "B",
    },
    {
        "question": "Was sind Bedingungen (if)?",
        "options": [
            "A) Prüfen, ob etwas wahr ist",
            "B) Wiederholen Code",
            "C) Speichern Werte",
        ],
        "answer": "A",
    },
    {
        "question": "Was ist None?",
        "options": [
            "A) Ein leerer Wert oder 'nichts'",
            "B) Eine Funktion",
            "C) Eine Schleife",
        ],
        "answer": "A",
    },
    {
        "question": "Was ist der Unterschied zwischen '=' und '=='?",
        "options": [
            "A) '=' weist zu, '==' vergleicht",
            "B) Beide sind gleich",
            "C) '=' vergleicht Zahlen",
        ],
        "answer": "A",
    },
    {
        "question": "Was bedeutet 'Datentyp'?",
        "options": [
            "A) Art eines gespeicherten Werts",
            "B) Ein Kommentar",
            "C) Eine Variable",
        ],
        "answer": "A",
    },

    # 21–30
    {
        "question": "Was ist eine Schleifenvariable?",
        "options": [
            "A) Eine globale Variable",
            "B) Eine Variable, die sich in einer Schleife ändert",
            "C) Eine Bedingung",
        ],
        "answer": "B",
    },
    {
        "question": "Was ist ein Index?",
        "options": [
            "A) Ein anderer Name für eine Funktion",
            "B) Die Position eines Elements (ab 0)",
            "C) Eine Textvariable",
        ],
        "answer": "B",
    },
    {
        "question": "Was bedeutet 'Slicing'?",
        "options": [
            "A) Einen Teil einer Liste oder Zeichenkette ausschneiden",
            "B) Eine Schleife abbrechen",
            "C) Eine Variable löschen",
        ],
        "answer": "A",
    },
    {
        "question": "Was ist eine Range?",
        "options": [
            "A) Eine Liste mit Text",
            "B) Eine Zahlenfolge",
            "C) Eine Funktion, die Strings vergleicht",
        ],
        "answer": "B",
    },
    {
        "question": "Was ist eine Bedingungskombination?",
        "options": [
            "A) Eine Schleife im if-Block",
            "B) Verbindung mehrerer Bedingungen mit and/or/not",
            "C) Ein anderer Name für eine Funktion",
        ],
        "answer": "B",
    },
    {
        "question": "Was sind Kommentare?",
        "options": [
            "A) Notizen im Code, die Python ignoriert",
            "B) Funktionen mit Textausgabe",
            "C) Variablen für Text",
        ],
        "answer": "A",
    },
    {
        "question": "Was sind Module?",
        "options": [
            "A) Schleifenvariablen",
            "B) Nur Zahlenlisten",
            "C) Externe oder eigene Python-Dateien mit Code",
        ],
        "answer": "C",
    },
    {
        "question": "Was ist eine Klasse?",
        "options": [
            "A) Eine einfache Funktion",
            "B) Eine Vorlage (Bauplan) für Objekte",
            "C) Eine Liste von Variablen",
        ],
        "answer": "B",
    },
    {
        "question": "Was sind Objekte?",
        "options": [
            "A) Konkrete Instanzen einer Klasse",
            "B) Nur Datentypen",
            "C) Textketten",
        ],
        "answer": "A",
    },
    {
        "question": "Was sind Parameter und Argumente?",
        "options": [
            "A) Platzhalter in Funktionen und die übergebenen Werte",
            "B) Nur Kommentare",
            "C) Logische Operatoren",
        ],
        "answer": "A",
    },

    # 31–35
    {
        "question": "Was ist der Unterschied zwischen lokal und global?",
        "options": [
            "A) Global: nur in Schleifen gültig",
            "B) Lokal: nur in Funktion gültig, global: im ganzen Programm",
            "C) Lokal: kann überall verwendet werden",
        ],
        "answer": "B",
    },
    {
        "question": "Was ist eine Exception (Fehlerbehandlung)?",
        "options": [
            "A) Ein Fehler, der abgefangen werden kann",
            "B) Eine Art Schleife",
            "C) Eine Textvariable",
        ],
        "answer": "A",
    },
    {
        "question": "Was ist eine verschachtelte Liste?",
        "options": [
            "A) Eine Liste, die andere Listen enthält",
            "B) Eine Liste aus Zahlen",
            "C) Eine Liste aus Strings",
        ],
        "answer": "A",
    },
    {
        "question": "Was macht len()?",
        "options": [
            "A) Gibt die Länge einer Liste oder Zeichenkette zurück",
            "B) Löscht eine Variable",
            "C) Wandelt Text in Zahlen um",
        ],
        "answer": "A",
    },
    {
        "question": "Was macht input()?",
        "options": [
            "A) Fragt Benutzereingaben ab",
            "B) Gibt Zufallszahlen zurück",
            "C) Beendet das Programm",
        ],
        "answer": "A",
    },
]
