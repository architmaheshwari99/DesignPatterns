from DesignPatterns.CarRentalSystem.models.reservations.registrations import Reservation
from DesignPatterns.CarRentalSystem.models.vehicle.vehicle import Vehicle


# At a given point in time, I want to know what all vehicles are present with me
# what vehicles are available and booked
# We will access this using the VehicleRepository
class VehicleInventory:
    def __init__(self, vehicle: Vehicle, reservation: Reservation = None):
        self.vehicle = vehicle
        self.reservation = reservation

        # Initialize the vehicle and reservation attributes on which you want to enable searching

