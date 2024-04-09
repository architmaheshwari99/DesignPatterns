from DesignPatterns.CarRentalSystem.models.account.personal_info import PersonalInfo
from DesignPatterns.CarRentalSystem.models.common.address import Address


class Contact:
    def __init__(self, phone, email, address: Address, personal_info: PersonalInfo):
        self.phone = phone
        self.email = email
        self.address = address
        self.personal_info = personal_info
