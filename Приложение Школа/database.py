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

        # Создаем таблицу учеников, если она не существует
        cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            student_class TEXT,
                            name TEXT)''')

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

# Функция для добавления ученика в базу данных
def add_student(student_class, student_name):
    """Добавить ученика в базу данных."""
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO students (student_class, name) VALUES (?, ?)''',
                       (student_class, student_name))
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при добавлении ученика: {e}")

# Функция для получения учеников по классу
def get_students_by_class(student_class):
    """Получить список учеников для выбранного класса."""
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT name FROM students WHERE student_class = ?''', (student_class,))
        students = cursor.fetchall()

        conn.close()
        return [student[0] for student in students]  # Возвращаем только имена учеников

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при получении учеников по классу: {e}")

# Функция для получения всех учеников
def get_all_students():
    """Получить всех учеников из базы данных."""
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT student_class, name FROM students''')
        students = cursor.fetchall()

        conn.close()
        return students  # Список всех учеников с их классами

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при получении всех учеников: {e}")
