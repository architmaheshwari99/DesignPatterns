from abc import ABC

from DesignPatterns.ParkingLot.models.parking.constants import ParkingSpotType


class ParkingSpot(ABC):
    def __init__(self, id, spot_type: ParkingSpotType, is_free: bool = True):
        self.id = id
        self.spot_type = spot_type
        self.is_free = is_free
        self.vehicle = None

    def assign_vehicle(self, vehicle):
        self.is_free = False
        self.vehicle = vehicle

    def vacate_spot(self):
        self.is_free = True
        self.vehicle = None

