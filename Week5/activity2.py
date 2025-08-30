class Person:
    def __init__(self, name, address, age, id):
        self.name = name
        self.address = address
        self.age = age
        self.id = id


class Student(Person):
    def __init__(self, name, address, age, id, academic_record):
        super().__init__(name, address, age, id)
        self.academic_record = academic_record = academic_record


class Staff(Person):
    def __init__(self, name, address, age, id, tax_code):
        super().__init__(name, address, age, id)
        self.tax_code = tax_code


class AcademicStaff(Staff):
    def __init__(self, name, address, age, id, tax_code, salary):
        super().__init__(name, address, age, id, tax_code)
        self.salary = salary


class GeneralStaff(Staff):
    def __init__(self, name, address, age, id, tax_code, pay_rate):
        super().__init__(name, address, age, id, tax_code)
        self.pay_rate = pay_rate