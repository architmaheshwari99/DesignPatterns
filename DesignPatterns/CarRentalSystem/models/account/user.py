from DesignPatterns.CarRentalSystem.models.account.account import Account
from DesignPatterns.CarRentalSystem.models.account.license_info import LicenseInfo


class User(Account):
    def __init__(self, *args, license_info: LicenseInfo = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._license_info = license_info

    @property
    def license_info(self):
        return self._license_info

    @license_info.setter
    def license_info(self, value):
        self._license_info = value


class Driver(Account):
    def __init__(self, *args, license_info: LicenseInfo = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._license_info = license_info

    @property
    def license_info(self):
        return self._license_info

    @license_info.setter
    def license_info(self, value):
        self._license_info = value


class Admin(Account):
    pass
