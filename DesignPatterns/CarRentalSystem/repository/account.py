from abc import ABC, abstractmethod

from DesignPatterns.CarRentalSystem.models.account.account import Account
from DesignPatterns.CarRentalSystem.models.account.constants import AccountType


class AccountRepository(ABC):

    @abstractmethod
    def create_account(self, account: Account):
        pass

    def reset_password(self, user_id: str, password: str):
        pass


class DriverRepository(AccountRepository):
    def __init__(self):
        super().__init__()  # Call parent class initializer if needed
        self.drivers = []
        self.account_map = {}

    def create_account(self, account: Account):
        pass


class AdminRepository(AccountRepository):
    def __init__(self):
        super().__init__()  # Call parent class initializer if needed
        self.admins = []
        self.account_map = {}

    def create_account(self, account: Account):
        pass


class UserRepository(AccountRepository):
    def __init__(self):
        super().__init__()  # Call parent class initializer if needed
        self.users = []
        self.account_map = {}

    def create_account(self, account: Account):
        pass

    def get_hired_vehicles(self, user_id, start_date, end_date):
        pass



class AccountRepositoryFactory:
    @staticmethod
    def mapping():
        return {
            AccountType.USER: UserRepository,
            AccountType.ADMIN: AdminRepository,
            AccountType.Driver: DriverRepository,
        }

    def get_account_repository(self, account_type: AccountType):
        return self.mapping()[account_type]
