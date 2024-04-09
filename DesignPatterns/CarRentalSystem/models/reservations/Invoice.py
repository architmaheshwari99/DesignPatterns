class Invoice:
    def __init__(self, invoice_id, reservation_id, user_id, user_charges, add_on_cost, add_on_services_cost, taxes,
                 total):
        self._invoice_id = invoice_id
        self._reservation_id = reservation_id
        self._user_id = user_id
        self._user_charges = user_charges
        self._add_on_cost = add_on_cost
        self._add_on_services_cost = add_on_services_cost
        self._taxes = taxes
        self._total = total
