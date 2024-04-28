class __Building:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(__Building, cls).__new__(cls)
        return cls.__instance


class Building(metaclass=__Building):
    def __init__(self):
        self.floors = []
        self.elevators = []