from collections import defaultdict

from DesignPatterns.ParkingLot.models.parking.constants import ParkingModelType


class ParkingFloor:
    def __init__(self, floor_id):
        self.floor_id = floor_id
        self.spots_map = {ParkingModelType.STANDARD: [defaultdict(list)], ParkingModelType.VALET: [defaultdict(list)],
                          ParkingModelType.PREMIUM: [defaultdict(list)], }
        self.used_spots = {}

    def is_floor_full(self):
        pass

    def get_spot_type_for_vehicle(self, vehicle_type, spot_type, spot_model):
        pass

    def park_vehicle(self, vehicle, spot_model):
        pass

    def vacate_spot(self, spot):
        pass
