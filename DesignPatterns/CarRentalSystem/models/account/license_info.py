from datetime import date

from DesignPatterns.CarRentalSystem.models.account.constants import LicenseType


class LicenseInfo:
    def __init__(self, license_number: str, issue_date: date, expiry_date: date, issued_at_place: str,
                 issued_in_state: str,
                 issued_in_country: str, license_type: LicenseType):
        self.license_number = license_number
        self.issue_date = issue_date
        self.expiry_date = expiry_date
        self.issued_at_place = issued_at_place
        self.issued_in_country = issued_in_country
        self.license_type = license_type
        self.issued_in_state = issued_in_state
