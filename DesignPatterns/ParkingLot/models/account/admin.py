from DesignPatterns.ParkingLot.models.account.account import Account
from DesignPatterns.ParkingLot.models.account.constants import AccountType


class Admin(Account):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._account_type = AccountType.ADMIN

    def add_floors(self):
        pass

    def add_spots(self):
        pass

    def add_attendants(self):
        pass

    def add_valets(self):
        pass
