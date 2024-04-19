from DesignPatterns.ParkingLot.models.account.constants import AccountType
from DesignPatterns.ParkingLot.models.common.address import Address
from DesignPatterns.ParkingLot.models.parking.parking_lot import ParkingLot
from DesignPatterns.ParkingLot.repository.accounts import AccountRepository


class ParkingLotApplication:

    def create_parking_lot(self):
        # Create Parking Lot
        parking_lot = ParkingLot(1, Address('line 1', 'line2', 'pincode', 'country'))

        # Create admin and add it to the employees of the respective parking lot
        account_repo = AccountRepository()
        admin = account_repo.get_or_create_user('admin', 'password', AccountType.ADMIN)
        account_repo.assign_to_parking_lot(parking_lot, admin)


        # Create parking spots
        # create parking floors, add the spot in the parking floor
        # add the parking floor to the parking lot
        admin.add_floors()


if __name__ == '__main__':
    parking_lot = ParkingLotApplication()
    parking_lot.create_parking_lot()
    parking_lot.