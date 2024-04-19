from DesignPatterns.ParkingLot.models.parking.constants import ParkingModelType
from DesignPatterns.ParkingLot.models.parking.parking_rate import ParkingRate


class StandardParkingRate(ParkingRate):
    def __init__(self, daily_cost, hourly_cost, description):
        super().__init__(daily_cost, hourly_cost, description=description)
        self.parking_model_type = ParkingModelType.STANDARD



class ValetParkingRate(ParkingRate):
    def __init__(self, daily_cost, hourly_cost, description):
        super().__init__(daily_cost, hourly_cost, description=description)
        self.parking_model_type = ParkingModelType.VALET



class PremiumParkingRate(ParkingRate):
    def __init__(self, daily_cost, hourly_cost, description):
        super().__init__(daily_cost, hourly_cost, description=description)
        self.parking_model_type = ParkingModelType.PREMIUM



class WeekendParkingRate(ParkingRate):
    def __init__(self, parking_rate, add_on_daily_cost, add_on_hourly_cost, description):
        self.parking_model_type = ParkingModelType.WEEKEND
        self.parking_rate = parking_rate
        self.add_on_hourly_cost = add_on_hourly_cost
        self.description = description
        self.add_on_daily_cost = add_on_daily_cost

    def get_cost(self, start_date_time, end_date_time):
        # add the addon for weekend by determining the number of overlapping hours and days of weekend
        return self.parking_rate.get_cost()
