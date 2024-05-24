from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def set_base(self) -> None:
        pass

    @abstractmethod
    def set_sauce(self) -> None:
        pass

    @abstractmethod
    def set_cheese(self) -> None:
        pass
    
    @abstractmethod
    def set_toppings(self) -> None:
        pass


class PizzaBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Pizza()

    @property
    def product(self) -> Pizza:
        product = self._product
        self.reset()

        return product

    def set_base(self, is_integral=False) -> None:
        if is_integral:
            self._product.add("Wheat integral base")

        self._product.add("Wheat base")

    def set_sauce(self) -> None:
        self._product.add("Tomatoes sauce")
    
    def set_cheese(self) -> None:
        self._product.add("Mozzarella cheese")

    def set_toppings(self) -> None:
        self._product.add("Toppings")


class PanzerottiBuilder(Builder):
    def __init__(self) -> None:
        self.reset()
    
    def reset(self) -> None:
        self._product = Panzerotti()
    
    @property
    def product(self) -> Panzerotti:
        product = self._product
        self.reset()

        return product

    def set_base(self, is_integral=False) -> None:
        if is_integral:
            self._product.add("Wheat integral base")

        self._product.add("Wheat base")

    def set_sauce(self) -> None:
        self._product.add("Tomatoes sauce")
    
    def set_cheese(self) -> None:
        self._product.add("Ricotta cheese")

    def set_toppings(self) -> None:
        self._product.add("Toppings")


class Pizza():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Pizza parts 🍕: {', '.join(self.parts)}", end="")


class Panzerotti():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Panzerotti parts (inside the wheat 🥟): {', '.join(self.parts)}", end="")


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.set_base()

    def build_full_featured_product(self) -> None:
        self.builder.set_base()
        self.builder.set_sauce()
        self.builder.set_cheese()
        self.builder.set_toppings()    
    
    def build_full_featured_integral_product(self) -> None:
        self.builder.set_base(is_integral=True)
        self.builder.set_sauce()
        self.builder.set_cheese()
        self.builder.set_toppings()


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    pizza_builder = PizzaBuilder()
    director.builder = pizza_builder

    print("Standard basic pizza: ")
    director.build_minimal_viable_product()
    pizza_builder.product.list_parts()

    print("\n")

    print("Standard full featured pizza: ")
    director.build_full_featured_product()
    pizza_builder.product.list_parts()

    print("\n")

    panzerotti_builder = PanzerottiBuilder()
    director.builder = panzerotti_builder

    print("Standard full featured panzerotti: ")
    director.build_full_featured_product()
    panzerotti_builder.product.list_parts()

    print("\n")

    print("Standard full featured integral panzerotti: ")
    director.build_full_featured_integral_product()
    panzerotti_builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    pizza_builder.set_base()
    pizza_builder.set_cheese()
    pizza_builder.product.list_parts()
