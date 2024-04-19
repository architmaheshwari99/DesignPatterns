class Archit:
    def __init__(self, age, is_hot):
        self._age = age
        self.__is_hot = is_hot

if __name__ == '__main__':
    a = Archit(25, True)
    print(a.age)