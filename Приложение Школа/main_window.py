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
        self.root.title(f"Личный кабинет - {user[1]}")
        self.root.geometry("500x400")

        # Заголовок
        self.label = tk.Label(self.root, text=f"Добро пожаловать, {user[1]}!", font=("Arial", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=20)

        # Кнопки действий
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.grid(row=1, column=0, columnspan=2, pady=10)

        actions = [
            ("Посмотреть домашнее задание", self.view_homework),
            ("Скинуть домашнее задание", self.submit_homework),
            ("Посмотреть посещаемость", self.view_attendance),
            ("Посмотреть расписание", self.view_schedule),
            ("Посмотреть успеваемость", self.view_grades),
            ("Чат с преподавателем", self.chat_with_teacher),
        ]

        # Размещение кнопок в сетке
        row, col = 0, 0
        for text, command in actions:
            btn = tk.Button(self.buttons_frame, text=text, width=30, command=command, font=('Arial', 12), bg="#4CAF50", fg="white")
            btn.grid(row=row, column=col, pady=5, padx=5)
            row += 1
            if row > 2:  # после 3 кнопок начинаем новую колонку
                row = 0
                col += 1

        # Кнопка выхода
        self.button_logout = tk.Button(self.root, text="Выйти", font=('Arial', 14), width=20, bg="#f44336", fg="white", command=self.logout)
        self.button_logout.grid(row=2, column=0, columnspan=2, pady=20)

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

    def logout(self):
        """Закрыть окно и вернуться на экран авторизации."""
        self.root.destroy()
        from login_window import LoginWindow
        root = tk.Tk()
        login_window = LoginWindow(root)
        login_window.run()
