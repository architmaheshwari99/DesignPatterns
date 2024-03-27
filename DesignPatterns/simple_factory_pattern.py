"""
    When we are creating objects(for example using new keyword) in concrete classes, we are
    breaking the rule: program to an interface, not in implementation.
    We should look in our program about what is constant and what can be changing(code modifications in near future)
    In the below program we are using a simple factory, outsourcing the object creation from the concrete class.

"""
from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def cut(self):
        pass

    @abstractmethod
    def box(self):
        pass

class CheesePizza(Pizza):
    def prepare(self):
        print('Preparing cheese pizza')

    def bake(self):
        print('Baking cheese pizza')

    def cut(self):
        print('Cutting cheese pizza')

    def box(self):
        print('Packing cheese pizza')


class CornPizza(Pizza):
    def prepare(self):
        print('Preparing corn pizza')

    def bake(self):
        print('Baking corn pizza')

    def cut(self):
        print('Cutting corn pizza')

    def box(self):
        print('Packing corn pizza')


class PizzaFactory:
    def create_pizza(self, pizza_type):
        if pizza_type == 'Cheese':
            return CheesePizza()
        elif pizza_type == 'Corn':
            return CornPizza()
        else:
            return None

class PizzaStore:
    pizza_factory: PizzaFactory = None
    def __init__(self, pizza_factory: PizzaFactory):
        self.pizza_factory = pizza_factory

    def order_pizza(self, pizza_type):
        pizza = self.pizza_factory.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.box()

if __name__ == '__main__':
    pizza_factory = PizzaFactory()
    pizza_store = PizzaStore(pizza_factory)
    pizza_store.order_pizza("Cheese")