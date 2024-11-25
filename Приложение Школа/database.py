#database.py

import sqlite3

def initialize_database():
    """Функция для инициализации базы данных, создания необходимых таблиц."""
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        # Создаем таблицу пользователей, если она не существует
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            birthdate TEXT,
                            contact TEXT,
                            student_class TEXT,
                            login TEXT,
                            password TEXT)''')

        # Если нужно, можно добавить другие таблицы или подготовить данные

        # Сохраняем изменения и закрываем соединение
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при инициализации базы данных: {e}")

def add_user(name, birthdate, contact, student_class, login, password):
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO users (name, birthdate, contact, student_class, login, password) 
                          VALUES (?, ?, ?, ?, ?, ?)''',
                          (name, birthdate, contact, student_class, login, password))

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при добавлении пользователя: {e}")

def authenticate_user(login, password):
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM users WHERE login = ? AND password = ?''', (login, password))
        user = cursor.fetchone()

        conn.close()

        if user:
            return user
        else:
            return None

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при аутентификации пользователя: {e}")
