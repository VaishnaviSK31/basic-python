from abc import ABC,abstractmethod
class Engine(ABC):
    @abstractmethod
    def start(self):...
    @abstractmethod
    def stop(self):...
class PetrolEngine(Engine):
    def start(self):
        print("Petrol Engine started")
    def stop(self):
        print("Petrol Engine stopped")
class DieselEngine(Engine):
    def start(self):
        print("Diesel Engine started")
    def stop(self):
        print("Diesel Engine stopped")
e:Engine=PetrolEngine()
e.start()
e.stop()