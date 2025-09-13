from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"


class Square(Shape):
    def draw(self):
        return "Drawing a Square"


class Triangle(Shape):
    def draw(self):
        return "Drawing a Triangle"


class ShapeFactory:
    __shapes = {
        'circle': Circle,
        'square': Square,
        'triangle': Triangle,
    }

    def create_shape(self, shape_type):
        if shape_type in self.__shapes:
            return self.__shapes[shape_type]()
        else:
            return None


factory = ShapeFactory()
shape = factory.create_shape("triangle")   
print(shape.draw())  
