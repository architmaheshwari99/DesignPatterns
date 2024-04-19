from DesignPatterns.ParkingLot.models.parking.constants import TicketStatus


class ParkingTicket:
    def __init__(self, id, vehicle, entry_time, spot, ticket_status: TicketStatus = TicketStatus.PARKED):
        self.id = id
        self.vehicle = vehicle
        self.entry_time = entry_time
        self.spot = spot
        self.ticket_status = ticket_status
        self.duration = 0
        self.charges = 0