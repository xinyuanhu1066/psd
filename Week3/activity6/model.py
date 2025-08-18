from database import DBBackend
import sys
import sqlite3


class Category:
    def add(self, name):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute('INSERT INTO categories (name) VALUES (?)', (name,))
        db.commit()
        print('Category added successfully.')
        db.close()

    def delete_by_id(self, id):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute('DELETE FROM categories WHERE id = ?', (id,))
        # Update Course table to set category_id column to NULL
        cursor.execute(
            'UPDATE courses SET category_id = NULL WHERE category_id = ?',
            (id,))
        db.commit()
        print('Category deleted successfully.')
        db.close()

    def all(self):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute('SELECT * FROM categories')
        result = cursor.fetchall()
        db.close()
        return result

    def view(self):
        result = self.all()
        if len(result) == 0:
            print('\nNo records.')
            return
        print()
        for record in result:
            print(record)


class Course:
    def add(self, title, timetable, category_id, lecturer_id, classroom_id):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute(
            'INSERT INTO courses '
            '(title, timetable, category_id, lecturer_id, classroom_id) '
            'VALUES (?, ?, ?, ?, ?)',
            (title, timetable, category_id, lecturer_id, classroom_id))
        db.commit()
        print('Course added successfully.')
        db.close()

    def delete_by_id(self, id):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute('DELETE FROM courses WHERE id = ?', (id,))
        # update many-to-many mapping table
        cursor.execute(
            'DELETE FROM course_registrations WHERE course_id = ?', (id,))
        # update Grade table
        cursor.execute('DELETE FROM grades WHERE course_id = ?', (id,))
        db.commit()
        print('Course deleted successfully.')
        db.close()

    def all(self):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute('SELECT * FROM courses')
        result = cursor.fetchall()
        db.close()
        return result

    def view(self):
        result = self.all()
        if len(result) == 0:
            print('\nNo records.')
            return
        print()
        for record in result:
            print(record)

    def get_reference(self, ref_name):
        """Return records of reference table."""
        # get current module object by looking up "__name__" in sys.modules
        current_module = sys.modules[__name__]
        # get class object by ref_name
        ref_class = getattr(current_module, ref_name)
        # create class instance
        ref_table = ref_class()
        return ref_table.all()
    
    def is_empty(self):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute('SELECT COUNT(*) FROM courses')
        count = cursor.fetchone()[0]
        db.close()
        return count == 0


class Classroom:
    def add(self, location, capacity):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute(
            'INSERT INTO classrooms (location, capacity) VALUES (?, ?)',
            (location, capacity))
        db.commit()
        print('Classroom added successfully.')
        db.close()

    def delete_by_id(self, id):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute('DELETE FROM classrooms WHERE id = ?', (id,))
        # Update Course table to set lecturer_id column to NULL
        cursor.execute(
            'UPDATE courses SET classroom_id = NULL WHERE classroom_id = ?',
            (id,))
        db.commit()
        print('Classroom deleted successfully.')
        db.close()

    def all(self):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute('SELECT * FROM classrooms')
        result = cursor.fetchall()
        db.close()
        return result

    def view(self):
        result = self.all()
        if len(result) == 0:
            print('\nNo records.')
            return
        print()
        for record in result:
            print(record)


class Lecturer:
    def add(self, name):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute('INSERT INTO lecturers (name) VALUES (?)', (name,))
        db.commit()
        print('Lecturer added successfully.')
        db.close()

    def delete_by_id(self, id):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute('DELETE FROM lecturers WHERE id = ?', (id,))
        # Update Course table to set lecturer_id column to NULL
        cursor.execute(
            'UPDATE courses SET lecturer_id = NULL WHERE lecturer_id = ?',
            (id,))
        db.commit()
        print('Lecturer deleted successfully.')
        db.close()

    def all(self):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute('SELECT * FROM lecturers')
        result = cursor.fetchall()
        db.close()
        return result

    def view(self):
        result = self.all()
        if len(result) == 0:
            print('\nNo records.')
            return
        print()
        for record in result:
            print(record)


class Student:
    def add(self, name, email):
        db = DBBackend()
        cursor = db.get_cursor()
        try:
            cursor.execute(
                'INSERT INTO students (name, email) VALUES (?, ?)', (name, email))
            db.commit()
            print('Student added successfully.')
        except sqlite3.IntegrityError:
            print('Adding student failed: email must be unique.')
        db.close()

    def delete_by_id(self, id):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute('DELETE FROM students WHERE id = ?', (id,))
        # update many-to-many mapping table
        cursor.execute(
            'DELETE FROM course_registrations WHERE student_id = ?', (id,))
        # update Grade table
        cursor.execute('DELETE FROM grades WHERE student_id = ?', (id,))
        db.commit()
        print('Student deleted successfully.')
        db.close()

    def all(self):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute('SELECT * FROM students')
        result = cursor.fetchall()
        db.close()
        return result

    def view(self):
        result = self.all()
        if len(result) == 0:
            print('\nNo records.')
            return
        print()
        for record in result:
            print(record)

    def register(self, student_id, course_id):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute(
            'INSERT INTO course_registrations '
            '(student_id, course_id) VALUES (?, ?)',
            (student_id, course_id))
        db.commit()
        print('Register course successfully.')
        db.close()

    def is_empty(self):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute('SELECT COUNT(*) FROM students')
        count = cursor.fetchone()[0]
        db.close()
        return count == 0


class Grade:
    def add(self, course_id, student_id, score):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute(
            'INSERT INTO grades '
            '(course_id, student_id, score) VALUES (?, ?, ?)',
            (course_id, student_id, score))
        db.commit()
        print('Grade added successfully.')
        db.close()

    def delete_by_id(self, id):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute('DELETE FROM grades WHERE id = ?', (id,))
        db.commit()
        print('Grade deleted successfully.')
        db.close()

    def all(self):
        db = DBBackend()
        cursor = db.get_cursor()
        cursor.execute('SELECT * FROM grades')
        result = cursor.fetchall()
        db.close()
        return result

    def view(self):
        result = self.all()
        if len(result) == 0:
            print('\nNo records.')
            return
        print()
        for record in result:
            print(record)

    def get_reference(self, ref_name):
        """Return records of reference table."""
        # get current module object by looking up "__name__" in sys.modules
        current_module = sys.modules[__name__]
        # get class object by ref_name
        ref_class = getattr(current_module, ref_name)
        # create class instance
        ref_table = ref_class()
        return ref_table.all()