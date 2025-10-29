from abc import ABC, abstractmethod
class Vehice(ABC):
    @abstractmethod
    def drive(self):
        pass
class Car(Vehice):
    def drive(self):
        return 'driving a car'
class Bike(Vehice):
    def drive(self):
        return 'driving a bike'
class VehicleFactory:
    def creadteVehicle(self, vehicleType):
        if vehicleType == 'car':
            return Car()
        if vehicleType(self, vehicleType) == 'bike':
            return Bike()
        else: 
            raise ValueError('unknow')
factory = VehicleFactory()
car = factory.creadteVehicle('car')
print(car.drive())