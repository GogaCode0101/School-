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

        # Создаем таблицу расписания, если она не существует
        cursor.execute('''CREATE TABLE IF NOT EXISTS schedules (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            schedule TEXT,
                            FOREIGN KEY (user_id) REFERENCES users(id))''')

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

def add_schedule(user_id, schedule_content):
    """Добавить расписание в базу данных."""
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO schedules (user_id, schedule) VALUES (?, ?)''',
                       (user_id, schedule_content))
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при добавлении расписания: {e}")

def get_schedule(user_id):
    """Получить расписание из базы данных."""
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT schedule FROM schedules WHERE user_id = ? ORDER BY id DESC LIMIT 1''', (user_id,))
        result = cursor.fetchone()

        conn.close()
        return result[0] if result else None

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при получении расписания: {e}")
