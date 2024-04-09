from datetime import date
from typing import List

from DesignPatterns.CarRentalSystem.models.common.address import Address
from DesignPatterns.CarRentalSystem.models.reservations.Addons import VehicleAddons, AddonService, ReservationStatus
from DesignPatterns.CarRentalSystem.models.vehicle.constants import VehicleType
from DesignPatterns.CarRentalSystem.models.vehicle.vehicle import Vehicle


class Reservation:
    def __init__(self, id, reservation_at, reservation_status: ReservationStatus, booking_start_time: date,
                 booking_end_time: date, pickup_location: Address, drop_address: Address,
                 odometer_at_start: int, fuel_at_start,
                 vehicle: Vehicle, vehicle_type: VehicleType, invoice_id=None, odometer_at_end: int = None,
                 fuel_at_end=None, vehicle_add_ons: List[VehicleAddons] = None,
                 add_on_services: List[AddonService] = None):
        self._id = id
        self._reservation_at = reservation_at
        self._reservation_status = reservation_status
        self._booking_start_time = booking_start_time
        self._booking_end_time = booking_end_time
        self._pickup_location = pickup_location
        self._drop_address = drop_address
        self._odometer_at_start = odometer_at_start
        self._fuel_at_start = fuel_at_start
        self._vehicle = vehicle
        self._vehicle_type = vehicle_type
        self._invoice_id = invoice_id
        self._odometer_at_end = odometer_at_end
        self._fuel_at_end = fuel_at_end
        self._vehicle_add_ons = vehicle_add_ons if vehicle_add_ons is not None else []
        self._add_on_services = add_on_services if add_on_services is not None else []
