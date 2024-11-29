from __future__ import annotations
from abc import ABC, abstractmethod


class Shape(ABC):
    def move(self, x, y):
        pass

    def draw(self, x, y):
        pass

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class Dot(Shape):
    def accept(self, visitor: Visitor):
        visitor.visit_dot(self)


class Circle(Shape):
    def accept(self, visitor: Visitor):
        visitor.visit_circle(self)


class Rectangle(Shape):
    def accept(self, visitor: Visitor):
        visitor.visit_rectangle(self)


class CompoundShape(Shape):
    def accept(self, visitor: Visitor):
        visitor.visit_compound_shape(self)


class Visitor(ABC):
    @abstractmethod
    def visit_dot(self, dot: Dot):
        pass

    @abstractmethod
    def visit_circle(self, circle: Circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle: Rectangle):
        pass

    @abstractmethod
    def visit_compound_shape(self, compound_shape: CompoundShape):
        pass


class XMLExportVisitor(Visitor):
    def visit_dot(self, dot: Dot):
        print(f'🫥 Export the dot"s ID and center coordinates {type(dot)}')

    def visit_circle(self, circle: Circle):
        print(f'🔵 Export the circle"s ID, center coordinates and radius {type(circle)}')

    def visit_rectangle(self, rectangle: Rectangle):
        print(f'🔳 Export the rectangle"s ID, left-top coordinatesm, width and height {type(rectangle)}')

    def visit_compound_shape(self, compound_shape: CompoundShape):
        print(f'🔷 Export the shape"s ID as well as the list of its children"s IDs {type(compound_shape)}')


if __name__ == '__main__':
    all_shapes = [Dot(), Rectangle(), Circle(), CompoundShape()]

    export_visitor = XMLExportVisitor()

    for shape in all_shapes:
        shape.accept(export_visitor)
