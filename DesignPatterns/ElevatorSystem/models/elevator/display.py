from abc import abstractmethod, ABC


class Display(ABC):
    def __init__(self, floor, capacity, direction):
        self.__floor = floor
        self.__capacity = capacity
        self.__direction = direction

    @abstractmethod
    def display(self):
        pass

class ElevatorDisplay(Display):
    def display(self):
        pass

class HallDisplay(Display):
    def display(self):
        pass
