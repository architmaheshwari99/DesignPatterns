class Note(ABC):
    def __init__(self, quantity):
        self.quantity = quantity
        self.denomination = None

class OneRupeeNote(Note):
    def __init__(self, quantity):
        self.quantity = quantity
        self.denomination = Note.ONE_RUPEE

class TenRupeeNote(Note):
    def __init__(self, quantity):
        self.quantity = quantity
        self.denomination = Note.TEN_RUPEE
