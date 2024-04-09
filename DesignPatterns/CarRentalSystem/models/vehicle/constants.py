from enum import Enum


class VehicleStatusChoice(Enum):
    AVAILABLE = 1
    UNAVAILABLE = 2
    BOOKED = 3
    SERVICING = 4


class VehicleCategory(Enum):
    PASSENGER = 1
    COMMERCIAL = 2


class VehicleType(Enum):
    LMV = 1
    MC = 2
    MCWG = 3


class FuelType(Enum):
    DIESEL = 1
    PETROL = 2
