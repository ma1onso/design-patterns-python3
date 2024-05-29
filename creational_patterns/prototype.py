# Note: It's possible implement the Prototype pattern using the copy and deepcopy methods: https://refactoring.guru/design-patterns/prototype/python/example
#  But the idea behind this example is to implement a from scratch example.
from abc import ABC, abstractmethod


class Shape(ABC):
  def __init__(self, source):
    self.X = getattr(source, 'X', None)
    self.Y = getattr(source, 'Y', None)
    self.color = getattr(source, 'color', None)

  @abstractmethod
  def clone(self):
    pass


class Rectangle(Shape):
  def __init__(self, source=None):
    """ source is a instance of Rectangle"""
    super().__init__(source)
    if source:
      self.width = source.width
      self.height = source.height
    else:
      self.width = None
      self.height = None

  def clone(self):
    return Rectangle(self)


class Circle(Shape):
  def __init__(self, source=None):
    """ source is a instance of Circle"""
    super().__init__(source)
    if source:
      self.radius = source.radius
    else:
      self.radius = None

  def clone(self):
    return Circle(self)


class Application:
  def __init__(self):
    self.shapes = []

    circle = Circle()
    circle.X = 10
    circle.Y = 10
    circle.radius = 20
    self.shapes.append(circle)

    another_circle = circle.clone()
    self.shapes.append(another_circle)

    rectangle = Rectangle()
    rectangle.width = 10
    rectangle.height = 20
    self.shapes.append(rectangle)

  def business_logic(self):
    shapes_copy = []
    for shape in self.shapes:
      shapes_copy.append(shape.clone())

    print('Assertions')
    print(f'First shape is equal (value) to cloned shape: {self.shapes[0].__dict__ == shapes_copy[0].__dict__}')
    print(f'First shape is equal (identity) to cloned shape: {self.shapes[0] is shapes_copy[0]}')
    
    print('#' * 10)

    print('Values')
    print(f'First shape is equal (value) to cloned shape: {self.shapes[0].__dict__} == {shapes_copy[0].__dict__}')
    print(f'First shape is equal (identity) to cloned shape: {id(self.shapes[0])} is {id(shapes_copy[0])}')

if __name__ == '__main__':
    # Example usage
    application = Application()
    application.business_logic()

