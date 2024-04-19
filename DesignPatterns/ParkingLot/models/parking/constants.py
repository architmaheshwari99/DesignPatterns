from enum import Enum


class ParkingSpotType(Enum):
    CAR, BIKE, ELECTRIC_CAR, ELECTRIC_BIKE, TRUCK, CYCLE = 1, 2, 3, 4, 5, 6


class ParkingModelType(Enum):
    STANDARD, PREMIUM, VALET, WEEKEND = 1, 2, 3, 4

class TicketStatus(Enum):
    PARKED, LOST, PAID, INVALID = 1, 2, 3, 4



class PaymentStatus(Enum):
    INITIATED, SUCCESSFUL, REFUNDED, FAILED = 1, 2, 3, 4