from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class OrderCommand(Command):
    """This command merge the command and receiver logic in one class"""
    def __init__(self, plates: str) -> None:
        self._plates = plates

    def execute(self) -> None:
        print(f'OrderCommand: See, I ordering your plates: {self._plates} to the Chef')


class FoodDeliveryCommand(Command):
    def __init__(self, receiver: Delivery, address: str):
        self._receiver = receiver
        self._address = address

    def execute(self) -> None:
        self._receiver.found_delivery_person()
        self._receiver.send_the_food(self._address)


# Receiver
class Delivery:
    def found_delivery_person(self) -> None:
        print('Looking for a person to send the food')
        print('Delivery person found')

    def send_the_food(self, address: str) -> None:
        print(f'Sending the food to the address: {address}')


# Sender (aka Invoker)
class ExecuteOrderAndDelivery:
    _order = None
    _delivery = None

    def set_order(self, command: Command):
        self._order = command

    def set_delivery(self, command: Command):
        self._delivery = command

    def do_order_and_delivery(self) -> None:
        if isinstance(self._order, Command):
            self._order.execute()

        if isinstance(self._delivery, Command):
            self._delivery.execute()


if __name__ == '__main__':
    invoker = ExecuteOrderAndDelivery()
    invoker.set_order(OrderCommand('Sourdough - Pizza'))
    
    receiver = Delivery()

    invoker.set_delivery(FoodDeliveryCommand(receiver, 'New York, Av. 1 #23'))
    invoker.do_order_and_delivery()