from __future__ import annotations
from abc import ABC, abstractmethod


# Transport + Engine + Controls
# Car + CombustionEngine + SteeringWheel
# Plane + JetEngine + Yoke


class TransportFactory(ABC):
    @abstractmethod
    def create_engine(self) -> AbstractEngine:
        pass

    @abstractmethod
    def create_controls(self) -> AbstractControls:
        pass


class CarFactory(TransportFactory):

    def create_engine(self) -> AbstractEngine:
        return CombustionEngine()

    def create_controls(self) -> AbstractControls:
        return SteeringWheel()


class PlaneFactory(TransportFactory):

    def create_engine(self) -> AbstractEngine:
        return JetEngine()

    def create_controls(self) -> AbstractControls:
        return Yoke()


class AbstractEngine(ABC):

    @abstractmethod
    def start(self) -> str:
        pass


class CombustionEngine(AbstractEngine):
    def start(self) -> str:
        return "Starting the Skyactive engine"


class JetEngine(AbstractEngine):
    def start(self) -> str:
        return "Starting the Concorde engine"


class AbstractControls(ABC):

    @abstractmethod
    def turn(self) -> None:
        pass

    @abstractmethod
    def start_button(self, collaborator: AbstractEngine) -> None:
        pass


class SteeringWheel(AbstractControls):
    def turn(self) -> str:
        return "Turning the steering wheel in the highway"

    def start_button(self, collaborator: AbstractEngine) -> str:
        result = collaborator.start()
        return f"The result of pressing the start button on the steering wheel ({result})"


class Yoke(AbstractControls):
    def turn(self) -> str:
        return "Turning the yoke flying"

    def start_button(self, collaborator: AbstractEngine):

        result = collaborator.start()
        return f"The result of pressing the start button on the yoke ({result})"


def client_code(factory: TransportFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    engine = factory.create_engine()
    controls = factory.create_controls()

    print(f"{controls.turn()}")
    print(f"{controls.start_button(engine)}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(CarFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(PlaneFactory())
