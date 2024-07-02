from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class CapuletEngine(Engine):
    def __init__(self, mileage):
        self.mileage = mileage

    def needs_service(self) -> bool:
        return self.mileage > 30000

class WilloughbyEngine(Engine):
    def __init__(self, mileage):
        self.mileage = mileage

    def needs_service(self) -> bool:
        return self.mileage > 60000

class SternmanEngine(Engine):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on
