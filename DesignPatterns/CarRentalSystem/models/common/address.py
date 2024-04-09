class Address:
    def __init__(self, line1, line2, street, city, country, pincode):
        self.line1 = line1
        self.line2 = line2
        self.street = street
        self.city = city
        self.country = country
        self.pincode = pincode


class Coordinates:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


class VehicleLocation:
    _address: Address
    _coordinates = Coordinates

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value):
        self._coordinates = value
