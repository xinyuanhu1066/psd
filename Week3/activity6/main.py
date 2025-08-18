from database import DBBackend
from model import *
import re


def menu():
    print('\n====== Elective Course Manager ======')
    print('1 Category')
    print('2 Course')
    print('3 Classroom')
    print('4 Lecturer')
    print('5 Student')
    print('6 Grade')
    print('7 Register Course')
    print('8 Exit')


def display_operations():
    print('\n--- Operations ---')
    print('a Add')
    print('d Delete')
    print('v View\n')


def prompt_parameters(table, params):
    """Prompt the user to input required attributes for a database table.
       Return values:
           True:  Correct input value
           False: The current attribute is a record ID of another table which is empty now.
                  The user should add new record to that table first.
    """
    for key, value in params.items():
        if type(value) == type(1):
            if key.endswith('_id'):
                ref_table_name = key[:-3].capitalize()
                result = table.get_reference(ref_table_name)
                if len(result) == 0:
                    print(f'\n{ref_table_name} is empty, you should add it first.')
                    return False
                else:
                    print(f'Available values for {key}:')
                    print()
                    for record in result:
                        print(record)
                    print()
                    while True:
                        user_value = input(f'Enter {key}: ').strip()
                        if re.match(r'^[0-9]+$', user_value):
                            user_value = int(user_value)
                            if user_value <= 0 or user_value > len(result):
                                print('Input number beyonds the index range. Try again.')
                            else:
                                break
                        else:
                            print('Invalid input, please try again.')
                    params[key] = user_value
            else:
                while True:
                    user_value = input(f'Enter {key}: ').strip()
                    if re.match(r'^[0-9]+$', user_value):
                        user_value = int(user_value)
                        if user_value <= 0:
                            print('Input number must be larger than 0. Try again.')
                        else:
                            break
                    else:
                        print('Invalid input, please try again.')
                params[key] = user_value
        else:
            user_value = input(f'Enter {key}: ').strip()
            params[key] = user_value
    return True


def main():
    DBBackend().create_tables()
    while True:
        menu()
        choice = input('\nPlease select a number[1-8]: ').strip()
        if choice == '8':
            print('Bye!')
            break
        elif choice == '7':
            student = Student()
            if student.is_empty():
                print('Student is empty, please add it first.')
                continue
            student.view()
            while True:
                student_id = input('Enter student id: ').strip()
                if re.match(r'^[0-9]+$', student_id):
                    student_id = int(student_id)
                    if student_id <= 0:
                        print('Input number must be larger than 0. Try again.')
                    else:
                        break
                else:
                    print('Invalid input, please try again.')
            course = Course()
            if course.is_empty():
                print('Course is empty, please add it first.')
                continue
            course.view()
            while True:
                course_id = input('Enter course id: ').strip()
                if re.match(r'^[0-9]+$', course_id):
                    course_id = int(course_id)
                    if course_id <= 0:
                        print('Input number must be larger than 0. Try again.')
                    else:
                        break
                else:
                    print('Invalid input, please try again.')
            student.register(student_id, course_id)
        elif re.match(r'^[1-6]$', choice):
            if choice == '1':
                target = Category()
                parameters = {'name': ''}
            elif choice == '2':
                target = Course()
                parameters = {
                    'title': '',
                    'category_id': 0,
                    'lecturer_id': 0,
                    'classroom_id': 0,
                    'timetable': '',
                }
            elif choice == '3':
                target = Classroom()
                parameters = {'location': '', 'capacity': 0}
            elif choice == '4':
                target = Lecturer()
                parameters = {'name': ''}
            elif choice == '5':
                target = Student()
                parameters = {'name': '', 'email': ''}
            elif choice == '6':
                target = Grade()
                parameters = {
                    'course_id': 0,
                    'student_id': 0,
                    'score': 0,
                }
            while True:
                display_operations()
                operation = input('Please select an operation[a,d,v]: ').strip().lower()
                if operation == 'a':
                    if prompt_parameters(target, parameters):
                        target.add(**parameters)
                    break
                elif operation == 'd':
                    delete_params = {'id': 0}
                    if prompt_parameters(target, delete_params):
                        target.delete_by_id(delete_params['id'])
                    break
                elif operation == 'v':
                    target.view()
                    break
                else:
                    print('Invalid input, please try again.')
        else:
            print('Invalid input, please try again.')



if __name__ == '__main__':
    main()