from abc import ABC

from DesignPatterns.CarRentalSystem.contants import BillStatusChoice


class Bill(ABC):
    def __init__(self, payment, registration, bill_status: BillStatusChoice, amount):
        self.amount = amount
        self.payment = payment
        self.registration = registration
        self.bill_status = bill_status
