from abc import ABC
from typing import Optional

from DesignPatterns.ParkingLot.models.account.constants import AccountType, AccountStatus
from DesignPatterns.ParkingLot.models.account.personal_info import PersonInfo
from DesignPatterns.ParkingLot.models.common.contact import ContactInfo


class Account(ABC):
    def __init__(self, user_name: str, password: str, account_type: AccountType = AccountType.STAFF, account_status: AccountStatus =AccountStatus.ACTIVE , personal_info: PersonInfo = None, contact_info: ContactInfo = None):
        self._user_name = user_name
        self._password = password
        self._account_type = account_type
        self._account_status = account_status
        self._personal_info: Optional[PersonInfo] = personal_info
        self._contact_info: Optional[ContactInfo] = contact_info

    @property
    def personal_info(self) -> PersonInfo:
        return self._personal_info

    @personal_info.setter
    def personal_info(self, value: PersonInfo):
        self._personal_info = value

    @property
    def contact_info(self) -> ContactInfo:
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value: ContactInfo):
        self._contact_info = value


