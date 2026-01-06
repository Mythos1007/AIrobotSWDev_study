from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def run(self):
        pass

class Taxi(Vehicle):
    def run(self):
        pass
    def __str__(self):
        return '자식 클래스 Taxi'
class Truck(Vehicle):
    def run(self):
        pass
    def __str__(self):
        return '자식 클래스 Truck'
class Bus(Vehicle):
    def run(self):
        pass
    def __str__(self):
        return '자식 클래스 Bus'
    
vehicles: list[Vehicle] = [Taxi(), Truck(), Bus()]

for vehicle in vehicles:
    vehicle.run()
    print(str(vehicle))

