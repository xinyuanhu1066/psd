What it is
==========
This project is a command line tool to manage college's elective course system. 
It stores the information of courses, lecturers, students, classrooms and grades into a SQLite3 database.
You can add, delete and view the records of the database from the single command line user interface.


Project structure
=================
- main.py: Entry point of the command line tool
- database.py: Define a DBBackend class to manage database connection and initialisation.
- model.py: Contains multiple classes for database entities. Each one implements table basic operations.


How to run
==========
1. Open a terminal, change to the project directory:

    cd psd/Week3/activity6

2. Run main.py:

    python main.py

The user interface looks like:

    ====== Elective Course Manager ======
    1 Category
    2 Course
    3 Classroom
    4 Lecturer
    5 Student
    6 Grade
    7 Register Course
    8 Exit

    Please select a number[1-8]: 2

    --- Operations ---
    a Add
    d Delete
    v View

    Please select an operation[a,d,v]: v

    (1, 'Linear Algebra', 'Monday 8:00~10:00', 1, 1, 1)

