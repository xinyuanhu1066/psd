## Project Scope
To enrich the students' knowledge base, the college provided many elective courses. 
The courses are grouped into di;erent categories. A Lecturer can provide multiple courses 
for more than one category.
A student can choose more than one courses based on his or her interests.
There are a few classrooms. One classroom can hold many elective courses.
The Lecturer of the course gives mark for each student and store it into the database.
The database on the back end should have the following entities:
• Course
• Category
• Student
• Lecturer
• Classroom
• Grade

## Actors
- Student
- Lecturer
- Administrator

## Use Cases
### Administrator
- Add classroom to the system
- Add course category
- Add lecturers and update their profiles

### Lecturer
- Add course to the system
- Choose a classroom for a course
- Choose category for a course
- Set timetable for a course
- Provide grade marks for students
- Calculate pass rate of a course
- Regrade second assessment attempt if mark is below 50%

### Student
- View all the courses
- View courses by category
- Select one or more courses
- View courses' grades
- Register and updates profile

## Use Case Diagram

![](usecases.drawio.png)