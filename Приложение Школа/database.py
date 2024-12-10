#database.py

import sqlite3
import os


def connect_to_db():
    """Функция для подключения к базе данных и получения курсора."""
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Ошибка подключения к базе данных: {e}")

def get_grades(user_id):
    """Получить все оценки для пользователя (ученика)."""
    try:
        conn = sqlite3.connect('school_database.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT subject, grade FROM grades WHERE user_id = ?''', (user_id,))
        grades = cursor.fetchall()

        conn.close()
        return grades  # Список всех оценок для пользователя

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при получении оценок: {e}")


def initialize_database():
    """Функция для инициализации базы данных, создания необходимых таблиц."""
    try:
        conn, cursor = connect_to_db()

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

        # Создаем таблицу оценок, если она не существует
        cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            subject TEXT,
                            grade TEXT,
                            FOREIGN KEY (user_id) REFERENCES users(id))''')

        # Создаем таблицу документов, если она не существует
        cursor.execute('''CREATE TABLE IF NOT EXISTS documents (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            filename TEXT,
                            file_content BLOB,
                            FOREIGN KEY (user_id) REFERENCES users(id))''')

        # Сохраняем изменения и закрываем соединение
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при инициализации базы данных: {e}")


# Функция для добавления оценки
def add_grade(user_id, subject, grade):
    """Добавить оценку в базу данных."""
    try:
        conn, cursor = connect_to_db()

        cursor.execute('''INSERT INTO grades (user_id, subject, grade) VALUES (?, ?, ?)''',
                       (user_id, subject, grade))
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при добавлении оценки: {e}")


def add_user(name, birthdate, contact, student_class, login, password):
    try:
        conn, cursor = connect_to_db()

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
        conn, cursor = connect_to_db()

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
        conn, cursor = connect_to_db()

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
        conn, cursor = connect_to_db()

        cursor.execute('''SELECT schedule FROM schedules WHERE user_id = ? ORDER BY id DESC LIMIT 1''', (user_id,))
        result = cursor.fetchone()

        conn.close()
        return result[0] if result else "Расписание не найдено"

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при получении расписания: {e}")


# Функция для добавления ученика в базу данных
def add_student(student_class, student_name):
    """Добавить ученика в базу данных."""
    try:
        conn, cursor = connect_to_db()

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
        conn, cursor = connect_to_db()

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
        conn, cursor = connect_to_db()

        cursor.execute('''SELECT student_class, name FROM students''')
        students = cursor.fetchall()

        conn.close()
        return students  # Список всех учеников с их классами

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при получении всех учеников: {e}")


# Функция для добавления документа в базу данных
def add_document(user_id, file_path):
    """Добавить документ в базу данных."""
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Файл {file_path} не найден.")

        with open(file_path, 'rb') as file:
            file_content = file.read()

        filename = os.path.basename(file_path)

        conn, cursor = connect_to_db()

        cursor.execute('''INSERT INTO documents (user_id, filename, file_content) 
                          VALUES (?, ?, ?)''', (user_id, filename, file_content))

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при добавлении документа: {e}")
    except FileNotFoundError as e:
        print(f"Ошибка файла: {e}")
        raise Exception(f"Произошла ошибка при добавлении документа: {e}")

def get_users():
    """Получить всех пользователей из базы данных."""
    try:
        conn, cursor = connect_to_db()

        cursor.execute('''SELECT id, name, birthdate, contact, student_class, login FROM users''')
        users = cursor.fetchall()

        conn.close()
        return users  # Список всех пользователей

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при получении всех пользователей: {e}")


# Функция для получения документа из базы данных
def get_document(user_id, document_id):
    """Получить документ по ID из базы данных."""
    try:
        conn, cursor = connect_to_db()

        cursor.execute('''SELECT filename, file_content FROM documents WHERE user_id = ? AND id = ?''',
                       (user_id, document_id))
        result = cursor.fetchone()

        conn.close()

        if result:
            filename, file_content = result
            with open(filename, 'wb') as file:
                file.write(file_content)
            return filename  # Возвращаем имя сохраненного файла
        else:
            return None

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        raise Exception(f"Произошла ошибка при получении документа: {e}")
