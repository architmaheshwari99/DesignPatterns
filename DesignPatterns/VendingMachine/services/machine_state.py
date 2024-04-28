from abc import ABC


class MachineState(ABC):
    def insert_cash(self, machine, note):
        raise NotImplemented()

    def select_product(self, machine, rack_code):
        raise NotImplemented()

    def get_change_if_required(self):
        raise NotImplemented()

    def dispense_product(self):
        raise NotImplemented()

    def update_inventory_state(self):
        raise NotImplemented()


