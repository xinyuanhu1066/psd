# Week 2 - Activity 6 : Develop a basic HR project using OO
# You are tasked with developing a simple program for the Human Resources (HR) department 
# to store and display basic employee information, including each employee’s name, salary, and job title.
# Requirements:
# Create at least two Employee objects with different data.
# Call the display_info() method to show each employee’s details.
# Call the give_raise() method to increase an employee’s salary and display the updated amount.
# Upload your completed project to GitHub and share the repository link by Friday, 15.8.25, 11:59 PM.
 
class Employee:
    def __init__(self, name, salary, title):
        self.name = name
        self.salary = salary
        self.job_title = title

    def display_info(self):
        """Print basic employee information."""
        # print the information using left alignment
        print('\n{:8s}{}'.format('Name:', self.name))
        print('{:8s}${}'.format('Salary:', self.salary))
        print('{:8s}{}\n'.format('Title:', self.job_title))

    def give_raise(self, amount):
        """Increase salary of current object and print the new value."""
        self.salary += amount
        print(f"{self.name}'s salary is increased to: ${self.salary}\n")


class EmployeeRecord:
    def __init__(self):
        # Use inner list to store multiple employee objects
        self.employees = []

    def add(self, employee):
        """Store employee object to inner list and print basic information."""
        self.employees.append(employee)
        employee.display_info()

    def get(self, index):
        """Return an employee object with index."""
        return self.employees[index]


# create EmployeeRecord object as a global variable to store employee information
record = EmployeeRecord()


if __name__ == '__main__':
    record.add(Employee('Jay', 90000, 'Software Engineer'))
    record.add(Employee('Kevin', 110000, 'Senior Software Engineer'))
    record.add(Employee('Tom', 120000, 'Full Stack Developer'))

    # Increase salary of the second employee in the record
    employee = record.get(1)
    employee.give_raise(1000)