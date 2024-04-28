from collections import defaultdict

from DesignPatterns.VendingMachine.services.WaitForMoneyState import WaitForMoneyState
from DesignPatterns.VendingMachine.services.inventory_service import InventoryService



class VendingMachine:
    def __init__(self, state=WaitForMoneyState()):
        self._state = state
        self.racks = []
        self.display = None
        self.inventory_service = InventoryService()
        self.cash_tray = defaultdict(list)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def add_product(self, product, rack):
        self.inventory_service.add_product(product, rack)

    def add_display(self, display):
        self.display = display

    def add_rack(self, rack):
        self.racks.append(rack)






