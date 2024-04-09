from abc import ABC
from typing import List

from DesignPatterns.CarRentalSystem.models.vehicle.vehicle import Vehicle


class Store(ABC):
    def __init__(self, id, name, location: Location, registration: List['Registration'], vehicles : List[Vehicle]):
        self.id = id
        self.name = name
        self.location = location
        self.registration = registration
        self.vehicles = vehicles