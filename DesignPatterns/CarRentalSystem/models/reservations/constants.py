from enum import Enum


class InsuranceType(Enum):
    PARTIAL = 1
    FULL = 2


class ReservationStatus(Enum):
    PENDING = 1
    COMPLETED = 2
