class AccountRepository:
    def __init__(self):
        self.admins = []
        self.staff = []
        self.valets = []
        self.employees = []

    def get_or_create_user(self, username, password, account_type):
        # find the user in self.employees and match the password
        # after the user is found, check the account type before returning
        pass

    def assign_to_parking_lot(self, parking_lot, employee):
        pass