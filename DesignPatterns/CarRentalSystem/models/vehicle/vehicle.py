from abc import ABC

from DesignPatterns.CarRentalSystem.models.common.address import VehicleLocation, Coordinates
from DesignPatterns.CarRentalSystem.models.vehicle.constants import VehicleCategory, VehicleStatusChoice, FuelType, \
    VehicleType
from DesignPatterns.CarRentalSystem.reviews import Reviews


# TODO: Make the fields not available during initialization null, create separate getter and setter for them

class Vehicle(ABC):
    def __init__(self, id: int, make: str, model: str, model_year: int, qr_code: str, number_of_seats: int,
                 vehicle_category: VehicleCategory, vehicle_type: VehicleType,
                 vehicle_status: VehicleStatusChoice = VehicleStatusChoice.UNAVAILABLE,
                 parked_location: VehicleLocation = None, current_location: Coordinates = None,
                 reviews: Reviews = None):
        self._id = id
        self._make = make
        self._model = model
        self._reviews = reviews if reviews else []
        self._model_year = model_year
        self._qr_code = qr_code
        self._number_of_seats = number_of_seats
        self._vehicle_category = vehicle_category
        self._vehicle_type = vehicle_type
        self._vehicle_status = vehicle_status
        self._parked_location = parked_location
        self._current_location = current_location

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

    @property
    def vehicle_status(self):
        return self._vehicle_status

    @vehicle_status.setter
    def vehicle_status(self, value):
        self._vehicle_status = value

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, value):
        self._reviews = value

    @property
    def number_of_seats(self):
        return self._number_of_seats

    @number_of_seats.setter
    def number_of_seats(self, value):
        self._number_of_seats = value

    @property
    def parked_location(self):
        return self._parked_location

    @parked_location.setter
    def parked_location(self, value):
        self._parked_location = value

    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def model_year(self):
        return self._model_year

    @model_year.setter
    def model_year(self, value):
        self._model_year = value

    @property
    def vehicle_category(self):
        return self._vehicle_category

    @vehicle_category.setter
    def vehicle_category(self, value):
        self._vehicle_category = value

    @property
    def current_location(self):
        return self._current_location

    @current_location.setter
    def current_location(self, value):
        self._current_location = value


class MotorVehicle(Vehicle, ABC):
    def __init__(self, id: int, make: str, model: str, reviews: Reviews, model_year: int, qr_code: str,
                 number_of_seats: int, fuel_type: FuelType,
                 vehicle_category: VehicleCategory, vehicle_status: VehicleStatusChoice,
                 parked_location: VehicleLocation, current_location: Coordinates, chassis_number, registration_number,
                 km_driven, mileage):
        self._chassis_number = chassis_number
        self._registration_number = registration_number
        self._km_driven = km_driven
        self._mileage = mileage
        self._fuel_type = fuel_type
        super(MotorVehicle, self).__init__(
            id=id, make=make, model=model, reviews=reviews, model_year=model_year, qr_code=qr_code,
            number_of_seats=number_of_seats, vehicle_category=vehicle_category, vehicle_status=vehicle_status,
            parked_location=parked_location, current_location=current_location
        )

    @property
    def chassis_number(self):
        return self._chassis_number

    @chassis_number.setter
    def chassis_number(self, value):
        self._chassis_number = value

    @property
    def registration_number(self):
        return self._registration_number

    @registration_number.setter
    def registration_number(self, value):
        self._registration_number = value

    @property
    def km_driven(self):
        return self._km_driven

    @km_driven.setter
    def km_driven(self, value):
        self._km_driven = value

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        self._mileage = value


class VehicleBuilder:
    def __init__(self, id: int):
        self._id = id
        self._make = None
        self._model = None
        self._reviews = None
        self._model_year = None
        self._qr_code = None
        self._number_of_seats = None
        self._vehicle_category = None
        self._vehicle_status = None
        self._parked_location = None
        self._current_location = None
        self._vehicle_type = None

    def set_vehicle_type(self, vehicle_type):
        self._vehicle_type = vehicle_type
        return self

    def set_make(self, make: str):
        self._make = make
        return self

    def set_model(self, model: str):
        self._model = model
        return self

    def set_reviews(self, reviews: Reviews):
        self._reviews = reviews
        return self

    def set_model_year(self, model_year: int):
        self._model_year = model_year
        return self

    def set_qr_code(self, qr_code: str):
        self._qr_code = qr_code
        return self

    def set_number_of_seats(self, number_of_seats: int):
        self._number_of_seats = number_of_seats
        return self

    def set_vehicle_category(self, vehicle_category: VehicleCategory):
        self._vehicle_category = vehicle_category
        return self

    def set_vehicle_status(self, vehicle_status: VehicleStatusChoice):
        self._vehicle_status = vehicle_status
        return self

    def set_parked_location(self, parked_location: VehicleLocation):
        self._parked_location = parked_location
        return self

    def set_current_location(self, current_location: Coordinates):
        self._current_location = current_location
        return self

    def build(self) -> Vehicle:
        return Vehicle(
            id=self._id, make=self._make, model=self._model, reviews=self._reviews, model_year=self._model_year,
            qr_code=self._qr_code, number_of_seats=self._number_of_seats, vehicle_category=self._vehicle_category,
            vehicle_status=self._vehicle_status, parked_location=self._parked_location,
            current_location=self._current_location
        )


class MotorVehicleBuilder:
    def __init__(self, id: int):
        self.vehicle_builder = VehicleBuilder(id)
        self._chassis_number = None
        self._registration_number = None
        self._km_driven = None
        self._mileage = None
        self._fuel_type = None

    # Setter methods specific to MotorVehicleBuilder

    def set_fuel_type(self, fuel_type: FuelType):
        self._fuel_type = fuel_type
        return self

    def set_chassis_number(self, chassis_number: str):
        self._chassis_number = chassis_number
        return self

    def set_registration_number(self, registration_number: str):
        self._registration_number = registration_number
        return self

    def set_km_driven(self, km_driven: float):
        self._km_driven = km_driven
        return self

    def set_mileage(self, mileage: float):
        self._mileage = mileage
        return self

    # Setter methods inherited from VehicleBuilder

    def set_make(self, make: str):
        self.vehicle_builder.set_make(make)
        return self

    def set_model(self, model: str):
        self.vehicle_builder.set_model(model)
        return self

    def set_reviews(self, reviews: Reviews):
        self.vehicle_builder.set_reviews(reviews)
        return self

    def set_model_year(self, model_year: int):
        self.vehicle_builder.set_model_year(model_year)
        return self

    def set_qr_code(self, qr_code: str):
        self.vehicle_builder.set_qr_code(qr_code)
        return self

    def set_number_of_seats(self, number_of_seats: int):
        self.vehicle_builder.set_number_of_seats(number_of_seats)
        return self

    def set_vehicle_category(self, vehicle_category: VehicleCategory):
        self.vehicle_builder.set_vehicle_category(vehicle_category)
        return self

    def set_vehicle_status(self, vehicle_status: VehicleStatusChoice):
        self.vehicle_builder.set_vehicle_status(vehicle_status)
        return self

    def set_parked_location(self, parked_location: VehicleLocation):
        self.vehicle_builder.set_parked_location(parked_location)
        return self

    def set_current_location(self, current_location: Coordinates):
        self.vehicle_builder.set_current_location(current_location)
        return self

    # Other setter methods from VehicleBuilder can be added here as needed

    def build(self) -> MotorVehicle:
        vehicle = self.vehicle_builder.build()
        return MotorVehicle(
            id=vehicle.id, make=vehicle.make, model=vehicle.model, reviews=vehicle.reviews,
            model_year=vehicle.model_year, qr_code=vehicle.qr_code, number_of_seats=vehicle.number_of_seats,
            vehicle_category=vehicle.vehicle_category, vehicle_status=vehicle.vehicle_status,
            parked_location=vehicle.parked_location,
            chassis_number=self._chassis_number, registration_number=self._registration_number,
            km_driven=self._km_driven, mileage=self._mileage
        )
