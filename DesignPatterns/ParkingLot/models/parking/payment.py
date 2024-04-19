from datetime import datetime

from DesignPatterns.ParkingLot.models.parking.constants import PaymentStatus


class Payment:
    def __init__(self, id, parking_ticket, amount):
        self.id = id
        self.parking_ticket = parking_ticket
        self.amount = amount
        self.initiated_datetime = None
        self.completed_datetime = None
        self.payment_status = PaymentStatus.INITIATED

    def pay(self, parking_ticket, amount):
        # initiate Payment
        # change payment status
        # update completion time
        pass