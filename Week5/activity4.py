# Person is the top parent class, which contains the most common attributes.
class Person:
    def __init__(self, name, address, age, id):
        self.name = name
        self.address = address
        self.age = age
        self.id = id

    def greet(self):
        print('Greetings and felicitations from maestro', self.name)


# Student inherits from Person, adding new attribute academic_record
class Student(Person):
    def __init__(self, name, address, age, id, academic_record):
        # call super() to initialise the attributes in parent class
        super().__init__(name, address, age, id)
        self.academic_record = academic_record = academic_record

    def greet(self):
        # Override greet() in parent class Person
        print("Hello! I'm a student from Yoobee College. My name is", self.name)


if __name__ == '__main__':
    student = Student('Mike', '15 Union St.', '22', '123456', 'academic record')
    # access the name attribute defined in parent class Person
    student.greet()