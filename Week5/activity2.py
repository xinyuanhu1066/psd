# Person is the top parent class, which contains the most common attributes.
class Person:
    def __init__(self, name, address, age, id):
        self.name = name
        self.address = address
        self.age = age
        self.id = id


# Student inherits from Person, adding new attribute academic_record
class Student(Person):
    def __init__(self, name, address, age, id, academic_record):
        # call super() to initialise the attributes in parent class
        super().__init__(name, address, age, id)
        self.academic_record = academic_record = academic_record


# Staff inherits from Person, adding new attribute tax_code
class Staff(Person):
    """Inherit from Person"""
    def __init__(self, name, address, age, id, tax_code):
        super().__init__(name, address, age, id)
        self.tax_code = tax_code


# AcademicStaff inherits from Staff, adding new attribute salary
class AcademicStaff(Staff):
    """Inherit from Staff"""
    def __init__(self, name, address, age, id, tax_code, salary):
        super().__init__(name, address, age, id, tax_code)
        self.salary = salary


# GeneralStaff inherits from Staff, adding new attribute pay_rate
class GeneralStaff(Staff):
    """Inherit from Staff"""
    def __init__(self, name, address, age, id, tax_code, pay_rate):
        super().__init__(name, address, age, id, tax_code)
        self.pay_rate = pay_rate


if __name__ == '__main__':
    student = Student('Mike', '15 Union St.', '22', '123456')
    # access the name attribute defined in parent class Person
    print(student.name)
    general_staff = GeneralStaff('21 Greys Avenue', '35', '112345', '567890', '100')
    # access the name attribute defined in grand parent class Person
    print(general_staff.name)
    # access the tax_code attribute defined in parent class Staff
    print(general_staff.tax_code)