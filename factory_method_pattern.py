"""
    The factory method pattern defines an interface for creating an object, but lets subclasses decide which class
    to instantiate. Factory pattern lets a class defer instantiation to subclass.
    Instantiation of objects can be dependent on some logic and we might want to compute it at runtime.

    Example: In the below example we have pizza stores in NY and Chicago, we want to create the pizza according to the
    store selected. We are assuming here all the stores have the same logic for preparing the pizza and we just need to
    outsource instantiation process. 

    Factory Pattern UML Diagram
----------------------------

1. Product (Interface/Abstract Class)
   |
   |  (implements/extends)
   |
   V
2. ConcreteProduct1, ConcreteProduct2, ... (Classes)
   (These classes implement the Product interface or extend the Product class)

3. Creator (Interface/Abstract Class)
   |
   |   (inherits)
   |
   V
4. ConcreteCreator1, ConcreteCreator2, ... (Classes)
   (These classes implement the Creator interface or extend the Creator class)
   (Each ConcreteCreator class is responsible for creating a specific product)

Relationships:
- ConcreteProduct classes implement or extend the Product interface/class.
- ConcreteCreator classes implement or extend the Creator interface/class.
- Each ConcreteCreator has a method (often named 'factoryMethod') that creates and returns an instance of a ConcreteProduct.

Note: A solid line with an arrow indicates inheritance or implementation.

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

class NYCheesePizza(Pizza):
    def prepare(self):
        print('Preparing NYCheesePizza')
        
    def bake(self):
        print('Baking NYCheesePizza')
        
    def cut(self):
        print('Cutting NYCheesePizza')
        
    def box(self):
        print('Boxing NYCheesePizza')


class NYCornPizza(Pizza):
    def prepare(self):
        print('Preparing NYCornPizza')

    def bake(self):
        print('Baking NYCornPizza')

    def cut(self):
        print('Cutting NYCornPizza')

    def box(self):
        print('Boxing NYCornPizza')

class ChicageCornPizza(Pizza):
    def prepare(self):
        print('Preparing ChicageCornPizza')

    def bake(self):
        print('Baking ChicageCornPizza')

    def cut(self):
        print('Cutting ChicageCornPizza')

    def box(self):
        print('Boxing ChicageCornPizza')


class ChicageCheesePizza(Pizza):
    def prepare(self):
        print('Preparing ChicageCheesePizza')

    def bake(self):
        print('Baking ChicageCheesePizza')

    def cut(self):
        print('Cutting ChicageCheesePizza')

    def box(self):
        print('Boxing ChicageCheesePizza')

class PizzaStore(ABC):
    pizza: Pizza = None

    def order_pizza(self, pizza_type):
        self.pizza = self.create_pizza(pizza_type)
        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()


    @abstractmethod
    def create_pizza(self, pizza_type):
        pass

class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type=='Cheese':
            return NYCheesePizza()
        elif pizza_type=='Corn':
            return NYCornPizza()
        else:
            raise NotImplementedError()
        
class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type=='Cheese':
            return ChicageCheesePizza()
        elif pizza_type=='Corn':
            return ChicageCornPizza()
        else:
            raise NotImplementedError()

if __name__ =='__main__':
    ny_pizza_store = NYPizzaStore()
    ny_pizza_store.order_pizza('Cheese')
    print('##############')
    chicago_pizza_store = ChicagoPizzaStore()
    chicago_pizza_store.order_pizza('Corn')




