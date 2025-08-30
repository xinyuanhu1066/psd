class Student:
    def __init__(self, name, age):
        self.name = name       # public​
        self._age = age        # protected​
        self.__grade = 'A'     # private​

    def get_grade(self):
        return self.__grade

    def get_grade_with_name(self):
        return f'{self.name}: {self.__grade}'
    
    def update_info(self):
        # change private attribute's value. It can be accessed because
        # it is defined in the current class
        self.__grade = 'A+'


class InternationalStudent(Student):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def get_age(self):
        # access the protected attribute defined in parent class
        return self._age


s = Student('Ali', 20)
print(s.name)         # accessible​
print(s._age)         # discouraged​
print(s.get_grade())  # correct way
print(s.get_grade_with_name())

s2 = InternationalStudent('Bob', 21)
print(s2.name)        # access the public attribute
print(s2.get_age())