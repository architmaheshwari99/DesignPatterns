from DesignPatterns.ParkingLot.models.account.account import Account
from DesignPatterns.ParkingLot.models.account.constants import AccountType


class Valet(Account):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._account_type = AccountType.VALET

    def park_car(self):
        pass