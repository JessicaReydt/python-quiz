# quiz/flet_app.py
from __future__ import annotations

import flet as ft
import time
import threading

from quiz.core import QuizEngine
from quiz.data import QUESTIONS


def main(page: ft.Page):
    # Fenster & App Settings
    page.window_width = 400
    page.window_height = 700
    page.window_resizable = False
    page.title = "🐍 Python Quiz"
    page.bgcolor = ft.Colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    accent = ft.Colors.CYAN_ACCENT_400
    text_color = ft.Colors.WHITE

    # UI Elemente
    title = ft.Text("🐍 Python Lern-Quiz", size=28, weight="bold", color=accent)
    question_text = ft.Text(size=20, color=text_color)
    feedback = ft.Text(size=18, color=text_color)
    progress_bar = ft.ProgressBar(width=350, value=0, color=accent)
    progress_text = ft.Text(size=16, color=ft.Colors.WHITE70)
    option_buttons = ft.Column(spacing=10, alignment="center")

    def start_screen(e=None):
        page.clean()

        start_btn = ft.ElevatedButton(
            "🚀 Quiz starten",
            on_click=start_quiz,
            width=250,
            height=50,
            bgcolor=accent,
            color="black",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=12),
                elevation=5,
            ),
        )

        start_container = ft.Container(
            content=ft.Column(
                [
                    title,
                    ft.Text("Teste dein Python-Wissen!", color=text_color, size=18),
                    start_btn,
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=350,
            height=600,
            bgcolor=ft.Colors.BLUE_GREY_900,
            border_radius=20,
            padding=20,
            alignment=ft.alignment.center,
        )
        page.add(start_container)

    def start_quiz(e):
        engine = QuizEngine(QUESTIONS)
        page.clean()
        page.add(
            ft.Container(
                content=ft.Column(
                    [title, progress_bar, progress_text, question_text, option_buttons, feedback],
                    spacing=15,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                width=350,
                height=600,
                bgcolor=ft.Colors.BLUE_GREY_900,
                border_radius=20,
                padding=20,
                alignment=ft.alignment.top_center,
            )
        )
        show_question(engine)

    def show_question(engine: QuizEngine):
        option_buttons.controls.clear()

        if not engine.has_finished():
            q = engine.current_question()
            idx = engine.current_index + 1

            question_text.value = f"{idx}. {q['question']}"
            progress_text.value = f"Frage {idx} von {engine.total}"
            progress_bar.value = engine.current_index / engine.total
            feedback.value = ""

            for option in q["options"]:
                btn = ft.ElevatedButton(
                    text=option,
                    width=300,
                    height=45,
                    bgcolor=ft.Colors.BLUE_GREY_800,
                    color=ft.Colors.WHITE,
                    style=ft.ButtonStyle(
                        elevation=3,
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                    on_click=lambda e, opt=option, eng=engine: check_answer(opt, eng),
                )
                option_buttons.controls.append(btn)

            page.update()
        else:
            show_result(engine)

    def check_answer(selected_option: str, engine: QuizEngine):
        result = engine.check_answer(selected_option)

        if result.is_correct:
            feedback.value = "✅ Richtig!"
            feedback.color = ft.Colors.GREEN_ACCENT_400
        else:
            feedback.value = f"❌ Falsch! Richtige Antwort: {result.correct_letter}"
            feedback.color = ft.Colors.RED_ACCENT_400

        page.update()

        def delayed_continue():
            time.sleep(0.8)
            engine.next()
            show_question(engine)

        threading.Thread(target=delayed_continue, daemon=True).start()

    def show_result(engine: QuizEngine):
        page.clean()
        percent = engine.percent()

        if percent == 1:
            msg, emoji, color = "Perfekt! Du bist ein echter Python-Profi!", "🏆", ft.Colors.GREEN_ACCENT_400
        elif percent >= 0.7:
            msg, emoji, color = "Sehr gut! Du hast Python schon gut verstanden.", "👏", ft.Colors.LIGHT_GREEN_ACCENT_400
        elif percent >= 0.4:
            msg, emoji, color = "Ganz ordentlich, aber etwas Übung schadet nicht.", "🙂", ft.Colors.AMBER_ACCENT_200
        else:
            msg, emoji, color = "Noch etwas lernen – du schaffst das!", "🤔", ft.Colors.RED_ACCENT_200

        result_text = ft.Text(
            f"{emoji} {msg}\nDu hast {engine.score} von {engine.total} richtig.",
            size=22,
            color=color,
            weight="bold",
            text_align="center",
        )

        restart_btn = ft.ElevatedButton(
            "🔁 Nochmal spielen",
            on_click=start_screen,
            width=250,
            height=50,
            bgcolor=accent,
            color="black",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=12),
                elevation=5,
                overlay_color=ft.Colors.CYAN_200,
            ),
        )

        result_container = ft.Container(
            content=ft.Column(
                [title, result_text, restart_btn],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=350,
            height=600,
            bgcolor=ft.Colors.BLUE_GREY_900,
            border_radius=20,
            padding=20,
            alignment=ft.alignment.center,
        )
        page.add(result_container)

    start_screen()


if __name__ == "__main__":
    ft.app(target=main)
