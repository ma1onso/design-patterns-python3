# Factory Method is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

from __future__ import annotations
from abc import ABC, abstractmethod


# Base class
class Logistic(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def delivery_plan(self) -> str:
        transport  = self.create_transport()

        result = f"Shipping the packages {transport.deliver()}"
        
        return result
    

class RoadLogistic(Logistic):
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistic(Logistic):
    def create_transport(self) -> Transport:
        return Ship()


# Base class
class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass
    

class Truck(Transport):
    def deliver(self) -> str:
        return "Driving a Tesla Truck"
    

class Ship(Transport):
    def deliver(self) -> str:
        return "Sailing the ocean"


def client_code(logistic_creator: Logistic) -> None:
    print(
        f"Client: I'm not aware of the logistic creator's class, but it still works.\n"
        f"{logistic_creator.delivery_plan()}", end=""
    )

if __name__ == "__main__":
    print("App: Launched with the RoadLogistic.")
    client_code(RoadLogistic())
    
    print("\n")
    
    print("App: Launched with the SeaLogistic.")
    client_code(SeaLogistic())
