from abc import abstractmethod, ABC


class Button(ABC):
    def __init__(self, status):
        self.__status = status

    def press_down(self):
        return None

    @abstractmethod
    def is_pressed(self):
        pass

class HallButton(Button):
    def __init__(self, button_sign):
        self.__button_sign = button_sign

    def is_pressed(self):
        pass

class ElevatorButton(Button):
    def __init__(self, destination_floor_number):
        self.__destination_floor_number = destination_floor_number

    def is_pressed(self):
        pass

