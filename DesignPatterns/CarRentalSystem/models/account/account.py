from abc import ABC

from DesignPatterns.CarRentalSystem.models.account.contact import Contact


class Account(ABC):
    def __init__(self, id_, email, username, password, last_accessed, account_status: AccountStatus,
                 contact: Contact = None):
        self._id = id_
        self._email = email
        self._username = username
        self._password = password
        self._last_accessed = last_accessed
        self._contact = contact
        self._account_status = account_status

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value
