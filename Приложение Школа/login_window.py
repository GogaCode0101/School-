#login_window.py

import tkinter as tk
from tkinter import messagebox
from database import authenticate_user
from student_interface import StudentInterface

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Авторизация")

        # Заголовок окна
        self.title_label = tk.Label(self.root, text="Авторизация", font=("Arial", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Логин и пароль
        self.login_label = tk.Label(self.root, text="Логин:")
        self.login_label.grid(row=1, column=0, padx=10, pady=5)
        self.login_entry = tk.Entry(self.root, width=30)
        self.login_entry.grid(row=1, column=1, padx=10, pady=5)

        self.password_label = tk.Label(self.root, text="Пароль:")
        self.password_label.grid(row=2, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.root, show="*", width=30)
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        # Кнопка для авторизации
        self.login_button = tk.Button(self.root, text="Войти", command=self.authenticate)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=10)

    def authenticate(self):
        login = self.login_entry.get()
        password = self.password_entry.get()

        # Проверка логина и пароля
        user = authenticate_user(login, password)
        if user:
            # Если авторизация успешна, переходим в личный кабинет
            self.root.destroy()  # Закрываем окно авторизации
            student_window = tk.Tk()
            student_interface = StudentInterface(student_window, user[1], user[4])  # Передаем имя и класс из базы
            student_interface.run()
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль!")

    def run(self):
        self.root.mainloop()
