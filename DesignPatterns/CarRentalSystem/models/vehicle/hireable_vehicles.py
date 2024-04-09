from DesignPatterns.CarRentalSystem.models.vehicle.vehicle import MotorVehicle, Vehicle, MotorVehicleBuilder


class Car(MotorVehicle):
    def __init__(self, id, make, model, reviews, model_year, qr_code, number_of_seats, vehicle_category,
                 vehicle_status, parked_location, current_location, chassis_number, registration_number,
                 km_driven, mileage):
        super().__init__(id, make, model, reviews, model_year, qr_code, number_of_seats, vehicle_category,
                         vehicle_status, parked_location, current_location, chassis_number, registration_number,
                         km_driven, mileage)


class CarBuilder(MotorVehicleBuilder):
    def __init__(self, id):
        super().__init__(id)

    def build(self):
        return Car(id=self.vehicle_builder._id, make=self.vehicle_builder._make, model=self.vehicle_builder._model,
                   reviews=self.vehicle_builder._reviews, model_year=self.vehicle_builder._model_year,
                   qr_code=self.vehicle_builder._qr_code, number_of_seats=self.vehicle_builder._number_of_seats,
                   vehicle_category=self.vehicle_builder._vehicle_category,
                   vehicle_status=self.vehicle_builder._vehicle_status,
                   parked_location=self.vehicle_builder._parked_location,
                   current_location=self.vehicle_builder._current_location,
                   chassis_number=self._chassis_number, registration_number=self._registration_number,
                   km_driven=self._km_driven, mileage=self._mileage)


class Bike(MotorVehicle):
    def __init__(self, id, make, model, reviews, model_year, qr_code, number_of_seats, vehicle_category,
                 vehicle_status, parked_location, current_location, chassis_number, registration_number,
                 km_driven, mileage):
        super().__init__(id, make, model, reviews, model_year, qr_code, number_of_seats, vehicle_category,
                         vehicle_status, parked_location, current_location, chassis_number, registration_number,
                         km_driven, mileage)


class MotorBikeBuilder(MotorVehicleBuilder):
    def __init__(self, id):
        super().__init__(id)

    def build(self):
        return Car(id=self.vehicle_builder._id, make=self.vehicle_builder._make, model=self.vehicle_builder._model,
                   reviews=self.vehicle_builder._reviews, model_year=self.vehicle_builder._model_year,
                   qr_code=self.vehicle_builder._qr_code, number_of_seats=self.vehicle_builder._number_of_seats,
                   vehicle_category=self.vehicle_builder._vehicle_category,
                   vehicle_status=self.vehicle_builder._vehicle_status,
                   parked_location=self.vehicle_builder._parked_location,
                   current_location=self.vehicle_builder._current_location,
                   chassis_number=self._chassis_number, registration_number=self._registration_number,
                   km_driven=self._km_driven, mileage=self._mileage)


class Cycle(Vehicle):
    def __init__(self, *aregs, **kwargs):
        super().__init__(*aregs, **kwargs)
