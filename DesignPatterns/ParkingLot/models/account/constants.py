from enum import Enum


class AccountType(Enum):
    ADMIN, ATTENDANT, VALET, STAFF = 1, 2, 3, 4

class AccountStatus(Enum):
    ACTIVE, INACTIVE, BLOCKED = 1, 2, 3