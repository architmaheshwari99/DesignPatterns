from enum import Enum


class RegistrationStatusChoice(Enum):
    REGISTERED = 'Registered'
    CONFIRMED = 'Confirmed'


class VehicleStatusChoice(Enum):
    AVAILABLE = "Available"
    UNAVAILABLE = "Unavailable"


class BillStatusChoice(Enum):
    SUCCESSFUL = "Successful"
    ERROR = "Error"
    REFUNDED = "Refunded"
