from typing import List

from DesignPatterns.CarRentalSystem.models.reservations.vehicle_inventory import VehicleInventory


class VehicleInventoryRepository:
    vehicle_inventory: List[VehicleInventory]

    def add_to_inventory(self, vehicle):
        pass

    def remove_from_inventory(self, vehicle):
        pass
