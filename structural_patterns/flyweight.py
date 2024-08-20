import random

from dataclasses import dataclass


# Flyweight class
@dataclass
class TreeType:
    name: str
    color: str
    texture: str

    def draw(self, canvas, x, y):
        print(f'Drawing the tree on x: {x} and y: {y} in canvas: {canvas} 🖼️')


# Flyweight factory
class TreeFactory:
    
    def __init__(self, tree_types=[]):
        self.tree_types = tree_types

    def get_tree_type(self, name, color, texture):
        tree_type = self._find_existing_free_type(name, color, texture)

        if tree_type == None:
            tree_type = TreeType(name, color, texture)
            self.tree_types.append(tree_type)

        return tree_type
    
    def _find_existing_free_type(self, name, color, texture):
        for tree_type in self.tree_types:
            if (tree_type.name, tree_type.color, tree_type.texture) == (name, color, texture):
                print(f'-> Existing tree type founded {name}-{color}-{texture} 😲')
                return tree_type
            
        return None


@dataclass
class Tree:
    x: int
    y: int
    tree_type: TreeType

    def draw(self, canvas):
        self.tree_type.draw(canvas, self.x, self.y)


class Forest:
    def __init__(self, trees=[]):
        self.trees = trees

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory().get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)

        print('Planting a tree 🌴')

        self.trees.append(tree)

    def draw(self, canvas):
        for tree in self.trees:
            tree.draw(canvas)


if __name__ == '__main__':
    forest = Forest()

    forest.plant_tree(3, 4, 'Palm', 'Green', 'palm.png')
    forest.plant_tree(10, 41, 'Palm', 'Green', 'palm.png')
    forest.plant_tree(2, 40, 'Passion fruit', 'Yellow', 'passion_fruit.png')

    forest.draw('Empty_canvas')