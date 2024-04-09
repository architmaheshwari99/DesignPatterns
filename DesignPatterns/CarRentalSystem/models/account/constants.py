from enum import Enum


class LicenseType(Enum):
    MCWG = 1
    MC = 2
    LMW = 3
    HMW = 4


class AccountStatus(Enum):
    ACTIVE = 1
    SUSPENDED = 2
    BLOCKED = 3
    BLACKLISTED = 4


class AccountType(Enum):
    USER = 1
    ADMIN = 2
    DRIVER = 3
