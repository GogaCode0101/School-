#main_window.py

import tkinter as tk
from tkinter import messagebox


class MainWindow:
    def __init__(self, root, user):
        """
        Конструктор главного окна после авторизации.
        :param root: Главное окно приложения.
        :param user: Информация о текущем пользователе.
        """
        self.root = root
        self.user = user
        self.root.title("Личный кабинет")
        self.root.geometry("400x400")

        # Заголовок
        self.label = tk.Label(self.root, text=f"Добро пожаловать, {user[1]}!", font=("Arial", 16))
        self.label.pack(pady=10)

        # Кнопки действий
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=20)

        actions = [
            ("Посмотреть домашнее задание", self.view_homework),
            ("Скинуть домашнее задание", self.submit_homework),
            ("Посмотреть посещаемость", self.view_attendance),
            ("Посмотреть расписание", self.view_schedule),
            ("Посмотреть успеваемость", self.view_grades),
            ("Чат с преподавателем", self.chat_with_teacher),
        ]

        for text, command in actions:
            btn = tk.Button(self.buttons_frame, text=text, width=30, command=command)
            btn.pack(pady=5)

    def view_homework(self):
        """Открыть окно для просмотра домашнего задания."""
        messagebox.showinfo("Домашнее задание", "Здесь можно увидеть домашнее задание!")

    def submit_homework(self):
        """Открыть окно для отправки домашнего задания."""
        messagebox.showinfo("Сдача домашнего задания", "Здесь можно сдать домашнее задание!")

    def view_attendance(self):
        """Открыть окно для просмотра посещаемости."""
        messagebox.showinfo("Посещаемость", "Здесь можно увидеть посещаемость!")

    def view_schedule(self):
        """Открыть окно для просмотра расписания."""
        messagebox.showinfo("Расписание", "Здесь можно увидеть расписание!")

    def view_grades(self):
        """Открыть окно для просмотра успеваемости."""
        messagebox.showinfo("Успеваемость", "Здесь можно увидеть успеваемость!")

    def chat_with_teacher(self):
        """Открыть окно чата с преподавателем."""
        messagebox.showinfo("Чат", "Здесь можно общаться с преподавателем!")
