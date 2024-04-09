from abc import ABC, abstractmethod
from enum import Enum

from DesignPatterns.CarRentalSystem.models.reservations.constants import InsuranceType


class AddonService(ABC):
    def __init__(self, id, name, description, price):
        self._id = id
        self._name = name
        self._description = description
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @abstractmethod
    @property
    def price(self):
        return self.get_price()

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @abstractmethod
    def get_price(self):
        pass


class Chauffeur(AddonService):
    def get_price(self):
        return 980


class Insurance(AddonService, ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._insurance_type = kwargs.pop('insurance_type')


class PartialInsurance(Insurance):
    def __init__(self, *args, **kwargs):
        kwargs.update({'insurance_type': InsuranceType.PARTIAL})
        super().__init__(*args, **kwargs)

    def get_price(self):
        return 300


class FullInsurance(Insurance):
    def __init__(self, *args, **kwargs):
        kwargs.update({'insurance_type': InsuranceType.FULL})
        super().__init__(*args, **kwargs)

    def get_price(self):
        return 600




class VehicleAddons(ABC):
    pass


class Navigation(VehicleAddons):
    def __init__(self, *args, **kwargs):
        self.__init__(*args, **kwargs)

    def get_price(self):
        return 100


class ChildSeat(VehicleAddons):
    def __init__(self, *args, **kwargs):
        self.__init__(*args, **kwargs)

    def get_price(self):
        return 150
