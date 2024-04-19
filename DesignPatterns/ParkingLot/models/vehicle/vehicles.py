from DesignPatterns.ParkingLot.models.vehicle.constants import VehicleType
from DesignPatterns.ParkingLot.models.vehicle.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._vehicle_type = VehicleType.CAR


class Bike(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._vehicle_type = VehicleType.BIKE


class ElectricCar(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._vehicle_type = VehicleType.ELECTRIC_CAR


class ElectricBike(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._vehicle_type = VehicleType.ELECTRIC_BIKE


class Cycle(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._vehicle_type = VehicleType.CYCLE


class Truck(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._vehicle_type = VehicleType.TRUCK
