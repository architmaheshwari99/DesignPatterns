class InventoryService:
    def __init__(self):
        self.products = []
        self.racks = []
        self.products = []

    def find_product(self, rack_code):
        # FInd rack if exists
        # CHeck if rack has any product left
        pass

    def get_products(self):
        return self.products

    def get_racks(self):
        return self.racks

    def add_product(self, product, rack):
        product.rack = rack
        rack.add_product(product)
        self.products.append(product)
