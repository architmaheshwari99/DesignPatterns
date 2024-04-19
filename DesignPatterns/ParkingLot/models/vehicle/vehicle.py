from abc import ABC

from DesignPatterns.CarRentalSystem.models.vehicle.constants import VehicleType


class Vehicle(ABC):
    def __init__(self, registration_number, vehicle_type: VehicleType):
        self._registration_number = registration_number
        self._vehicle_type = vehicle_type
        self._ticket = None
