"""
The Adapter Pattern’s role is to convert one interface into another.
 The Adapter Pattern converts the interface of a class into another interface the clients expect.
 Adapter lets classes work together that couldn’t otherwise because of incompatible interfaces.
 this pattern allows us to use a client with an incompatible interface by creating an Adapter that
 does the conversion. This acts to decouple the client from the implemented interface

 Target-> Duck
 Adapter-> TurkeyAdapter
 Adaptee-> Turkey

  Object adapters and class adapters are the two different means of adapting the adaptee (composition versus inheritance)

Object adapters uses composition to have the adaptee information
Class adapters uses inheritance and extend the adaptee and Target interface into an adapter

Make sure that you have at least two classes with incompatible interfaces:

A useful service class, which you can’t change (often 3rd-party, legacy or with lots of existing dependencies).
One or several client classes that would benefit from using the service class.
"""
from abc import ABC, abstractmethod


class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class MallardDuck(Duck):
    def quack(self):
        print("Quack")

    def fly(self):
        print("Fly")


class Turkey(ABC):
    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class WildTurkey(Turkey):
    def gobble(self):
        print("gobble")

    def fly(self):
        print("Fly")


class TurkeyAdapter(Duck):
    turkey: Turkey

    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        self.turkey.fly()
        self.turkey.fly()


class ClassTurkeyAdapter(Duck, Turkey):
    def quack(self):
        self.gobble()

    def fly(self):
        print("Fly")
        print("Fly")

    def gobble(self):
        print("gobble")


if __name__ == "__main__":
    duck = MallardDuck()
    duck.fly()
    duck.quack()
    print("////////////////////////////////")
    turkey = WildTurkey()
    turkey.gobble()
    turkey.fly()
    print("////////////////////////////////")
    adaptive_turkey = TurkeyAdapter(turkey)
    adaptive_turkey.quack()
    adaptive_turkey.fly()
    print("////////////////////////////////")

    class_turkey = ClassTurkeyAdapter()
    class_turkey.quack()
    class_turkey.fly()
