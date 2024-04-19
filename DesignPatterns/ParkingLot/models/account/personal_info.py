from DesignPatterns.ParkingLot.models.common.address import Address


class PersonInfo:
    def __init__(self, name, date_of_birth, gender, address: Address = None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.address = address