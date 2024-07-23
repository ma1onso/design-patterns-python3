from abc import ABC, abstractmethod
from typing import List


class Item(ABC):
    def __init__(self, price) -> None:
        self._price = price

    @abstractmethod
    def price(self):
        pass


class Product(Item):
    def identification(self):
        print(f'I"m the product with ID: {id(self)}')

    def price(self):
        return self._price


class Service(Product):
    def identification(self):
        print(f'I"m the service with ID: {id(self)}')


class Box(Item): # Box or Order
    def __init__(self) -> None:
        self._items: List[Item] = []

    def add(self, item: Item):
        self._items.append(item)

    def delete(self, item: Item):
        self._items.remove(item)

    def price(self):
        total_price = 0
        for item in self._items:
            total_price += item.price()

        return total_price



if __name__ == '__main__':
    order = Box()

    box_one = Box()
    box_one.add(Product(122))
    box_one.add(Product(234))

    box_two = Box()
    service = Service(122)
    box_two.add(service)

    order.add(box_one)
    order.add(box_two)

    print(f'Order total price: ${order.price()} 💸')

    print('Removing service from order... 🧨')
    box_two.delete(service)
    print(f'Updated order total price: ${order.price()} 💸')
