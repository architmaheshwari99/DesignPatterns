from DesignPatterns.ParkingLot.models.account.account import Account
from DesignPatterns.ParkingLot.models.account.constants import AccountType


class Attendant(Account):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._account_type = AccountType.Attribute

    def process_ticket(self):
        pass
