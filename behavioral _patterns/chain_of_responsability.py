from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class AbstractHandler(ABC):
    @abstractmethod
    def set_next(self, handler: AbstractHandler) -> AbstractHandler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class BaseHandler(AbstractHandler):
    _next_handler: AbstractHandler = None

    def set_next(self, handler: AbstractHandler) -> AbstractHandler:
        self._next_handler = handler

        return handler
    
    @abstractmethod
    def handle(self, request) -> str | None:
        if self._next_handler:
            return self._next_handler.handle(request)

        return super().handle(request)


# Concrete handlers
class MonkeyHandler(BaseHandler):
    def handle(self, request) -> str | None:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(BaseHandler):
    def handle(self, request) -> str | None:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(BaseHandler):
    def handle(self, request) -> str | None:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)
        

def client_code(handler: AbstractHandler) -> None:
    for food in ["Nut", "Banana", "Cup of coffe"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)

        if result:
            print(f"{result}", end="")
        else:
            print(f"{food} was left untouched.", end="")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)
