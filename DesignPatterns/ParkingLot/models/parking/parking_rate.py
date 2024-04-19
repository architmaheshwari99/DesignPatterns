from abc import ABC, abstractmethod

from DesignPatterns.ParkingLot.models.parking.constants import ParkingModelType


class ParkingRate(ABC):
    def __init__(self, daily_cost, hourly_cost, description, parking_model_type: ParkingModelType = ParkingModelType.STANDARD):
        self.parking_model_type = parking_model_type
        self.daily_cost = daily_cost
        self.hourly_cost = hourly_cost
        self.description = description


    def get_cost(self, start_date_time, end_date_time):
        pass