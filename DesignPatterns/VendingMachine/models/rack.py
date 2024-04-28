class Rack:
    def __init__(self, id):
        self.id = id
        self.products = []

    def get_products(self):
        return self.products

    def add_product(self, product):
        self.products.append(product)
        