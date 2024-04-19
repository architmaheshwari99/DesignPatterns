from DesignPatterns.ParkingLot.models.common.address import Address


class ParkingLot:
    def __init__(self, parking_lot_id, address: Address):
        self.parking_lot_id = parking_lot_id
        self.address = address

        self.parking_floors = []
        self.entry_panels = []
        self.exit_panels = []
        self.employees = []

    def is_full(self):
        # Check all the floors if they are full or not?
        pass

    def can_park(self):
        # Check for parking in all the floors
        pass

    def get_parking_spot(self, vehicle_type, spot_model):
        # based on different strategy, allot the parking spot
        pass

    def vacate_parking_spot(self, vehicle_spot):
        pass