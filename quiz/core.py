# quiz/core.py
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict, Any


Question = Dict[str, Any]


def _normalize_letter(text: str) -> str:
    return text.strip().upper()[:1]


@dataclass
class CheckResult:
    is_correct: bool
    correct_letter: str
    correct_option_text: str


class QuizEngine:
    def __init__(self, questions: List[Question]) -> None:
        if not questions:
            raise ValueError("questions darf nicht leer sein.")
        self._original_questions = questions
        self.questions = list(questions)
        self.current_index = 0
        self.score = 0

    def reset(self) -> None:
        """Quiz zurücksetzen (z.B. für 'Nochmal spielen')."""
        self.questions = list(self._original_questions)
        self.current_index = 0
        self.score = 0

    @property
    def total(self) -> int:
        return len(self.questions)

    def current_question(self) -> Question:
        return self.questions[self.current_index]

    def has_finished(self) -> bool:
        return self.current_index >= self.total

    def check_answer(self, selected: str) -> CheckResult:
        q = self.current_question()
        correct_letter = str(q["answer"]).strip().upper()

        selected_letter = _normalize_letter(selected)
        is_correct = selected_letter == correct_letter

        if is_correct:
            self.score += 1

        correct_option_text = ""
        for opt in q["options"]:
            opt_str = str(opt)
            if _normalize_letter(opt_str) == correct_letter:
                correct_option_text = opt_str
                break

        return CheckResult(
            is_correct=is_correct,
            correct_letter=correct_letter,
            correct_option_text=correct_option_text,
        )

    def next(self) -> None:
        self.current_index += 1

    def percent(self) -> float:
        return self.score / self.total
