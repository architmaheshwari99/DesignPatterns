import random
import string

from DesignPatterns.VendingMachine.controller.vending_machine import VendingMachine
from DesignPatterns.VendingMachine.models.constants import ProductType, Note
from DesignPatterns.VendingMachine.models.display import Display
from DesignPatterns.VendingMachine.models.product import Product
from DesignPatterns.VendingMachine.models.rack import Rack
from DesignPatterns.VendingMachine.services.SelectProductState import SelectProductState


class VendingMachineController:
    def __init__(self):
        self.vending_machine = VendingMachine()

    def create_and_add_products(self):
        racks = self.vending_machine.inventory_service.get_racks()
        products = self.vending_machine.inventory_service.get_products()

        for i in range(3):
            rack = Rack(i)
            self.vending_machine.add_rack(rack)

        for i in range(10):
            product_name = ''.join(random.choices(string.ascii_letters, k=5))
            product_description = ''.join(random.choices(string.ascii_letters, k=15))
            product_cost = random.randint(10, 30)
            if i < 3:
                product_type = ProductType.SNACKS
                rack = racks[0]
            elif i < 6:
                product_type = ProductType.BEVERAGE
                rack = racks[1]
            else:
                product_type = ProductType.OTHERS
                rack = racks[2]

            product = Product(i, product_name, product_description, product_cost, product_type)
            self.vending_machine.inventory_service.add_product(product, rack)


    def display_products(self):
        products = self.vending_machine.inventory_service.get_products()

        for product in products:
            print(f"{product.name} in {product.rack.id} at price {product.price}")




if __name__ == '__main__':
    vending_machine_controller = VendingMachineController()
    vending_machine_controller.create_and_add_products()
    vending_machine_controller.display_products()
    vending_machine_controller.vending_machine.add_display(Display())

    machine_state = vending_machine_controller.vending_machine.state
    machine_state.insert_coin(vending_machine_controller.vending_machine, Note.TEN_RUPEE)
    machine_state.insert_coin(vending_machine_controller.vending_machine, Note.TEN_RUPEE)

    vending_machine_controller.vending_machine.state = SelectProductState()
    machine_state.select_product(vending_machine_controller.vending_machine, 1)


    # vending_machine_controller.vending_machine.state = CancelTransactionState()

    vending_machine_controller.vending_machine.state = DispenseProduct()
    machine_state.dispense_product()

