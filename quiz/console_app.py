# quiz/console_app.py

from __future__ import annotations

from quiz.core import QuizEngine
from quiz.data import QUESTIONS


def ask_for_answer() -> str:
    """Fragt den Nutzer so lange, bis eine gültige Antwort (A/B/C) eingegeben wurde."""
    while True:
        answer = input("Deine Antwort (A/B/C): ").strip().upper()
        if answer in {"A", "B", "C"}:
            return answer
        print("Bitte gib nur A, B oder C ein.\n")


def main() -> None:
    engine = QuizEngine(QUESTIONS)

    print("🧠 Willkommen zum Python Multiple-Choice-Quiz!")
    print("Beantworte jede Frage mit A, B oder C.\n")

    while not engine.has_finished():
        q = engine.current_question()
        idx = engine.current_index + 1

        print(f"{idx}. {q['question']}")
        for opt in q["options"]:
            print(opt)

        user_answer = ask_for_answer()
        result = engine.check_answer(user_answer)

        if result.is_correct:
            print("✅ Richtig!\n")
        else:
            print(f"❌ Falsch! Richtige Antwort: {result.correct_letter}\n")

        engine.next()

    print("-" * 52)
    print(f"🎯 Du hast {engine.score} von {engine.total} Fragen richtig beantwortet!")
    print("-" * 52)

    p = engine.percent()
    if p == 1:
        print("🏆 Perfekt! Du bist ein echter Python-Profi!")
    elif p >= 0.7:
        print("👏 Sehr gut! Du hast Python schon gut verstanden.")
    elif p >= 0.4:
        print("🙂 Ganz ordentlich, aber etwas Übung schadet nicht.")
    else:
        print("🤔 Noch etwas lernen – du schaffst das!")


if __name__ == "__main__":
    main()
