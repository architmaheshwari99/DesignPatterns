from DesignPatterns.VendingMachine.services.machine_state import MachineState


class WaitForMoneyState(MachineState):

    def _verify_note(self, note):
        pass

    def insert_cash(self, machine, note):
        self._verify_note(note)
        machine.cash_tray[note] += 1
        machine.cash_tray_amount += note

    def select_product(self, machine, rack_code):
        raise NotImplemented()

    def get_change_if_required(self):
        raise NotImplemented()

    def dispense_product(self):
        raise NotImplemented()


