from DesignPatterns.ParkingLot.models.parking.constants import ParkingSpotType
from DesignPatterns.ParkingLot.models.parking.parking_spot import ParkingSpot


class CarParkingSpot(ParkingSpot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spot_type = ParkingSpotType.CAR


class ElectricCarParkingSpot(ParkingSpot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spot_type = ParkingSpotType.ELECTRIC_CAR


class BikeParkingSpot(ParkingSpot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spot_type = ParkingSpotType.BIKE


class ElectricBikeParkingSpot(ParkingSpot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spot_type = ParkingSpotType.ELECTRIC_BIKE


class TruckParkingSpot(ParkingSpot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spot_type = ParkingSpotType.TRUCK


class CycleBikeParkingSpot(ParkingSpot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spot_type = ParkingSpotType.CYCLE