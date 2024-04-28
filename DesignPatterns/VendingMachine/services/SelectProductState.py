from DesignPatterns.VendingMachine.services.machine_state import MachineState


class SelectProductState(MachineState):

    def _verify_note(self, note):
        pass

    def insert_cash(self, machine, note):
        raise NotImplemented()

    def select_product(self, machine, rack_code):
        machine.inventory.find_product(rack_code)

    def get_change_if_required(self):
        raise NotImplemented()

    def dispense_product(self):
        raise NotImplemented()