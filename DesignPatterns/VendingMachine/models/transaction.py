class Bill:
    def __init__(self, product, amount):
        self.product = product
        self.amount = amount
        self.ts = now()

class Transactions:
    def __init__(self):
        self.transactions = []

    def add_bill(self, bill):
        self.transactions.append(bill)