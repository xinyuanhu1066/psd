import sqlite3


class DBBackend:
    def __init__(self):
        self.conn = sqlite3.connect("elective_course_system.db")

    def get_cursor(self):
        return self.conn.cursor()
    
    def commit(self):
        self.conn.commit()
    
    def close(self):
        self.conn.close()

    def create_tables(self):
        """Create tables to map the relationships between
           Course, Category, Student, Lecturer, Classroom, Grade.
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS lecturers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS classrooms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                location TEXT NOT NULL,
                capacity INTEGER
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                timetable TEXT NOT NULL,
                category_id INTEGER REFERENCES categories(id),
                lecturer_id INTEGER REFERENCES lecturers(id),
                classroom_id INTEGER REFERENCES classrooms(id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER REFERENCES students(id),
                course_id INTEGER REFERENCES courses(id),
                score INTEGER
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS course_registrations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_id INTEGER REFERENCES courses(id),
                student_id INTEGER REFERENCES students(id)
            )
        ''')
        self.conn.close()