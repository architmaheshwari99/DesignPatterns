from enum import Enum


class Note(Enum):
    TEN_RUPEE, ONE_RUPEE = 10, 1


class Message(Enum):
    NO_BALANCE = 'NO BALANCE'
    NO_PRODUCT = 'NO PRODUCT'

class ProductType(Enum):
    BEVERAGE, SNACKS, OTHERS = 1, 2, 3
