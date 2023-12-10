"""
    The Abstract Factory Pattern provides an interface for creating families of related or dependent objects
    without specifying their concrete classes.

    Factory Method
    - Creates objects using Inheritance, to create object using factory method pattern you'll have to extend the class and
    override the factory method



    Abstract Factory
    - Creates objects using composition, provide an abstract type for creating a family of products. Subclasses
    of this type define how those products are produced.
    - It can also be called factories of factories and is used when we want to create multiple products, in multiple
    factories, we group logically similar classes
    - Abstract Factory internally uses Factory Method pattern

    Example: We have multiple pizza stores and each pizza store has a different way of creating the same pizza, the
    ingredients for creating the pizza depends on the location of the pizza store. For example the sauces used in pizza
    would be different in NY and Chicago etc.
    Steps for designing

    - Explicitly declare interfaces for each distinct product of the product family
        ~ As we have different ingredients in Pizza, we will create an interface for
        all the distinct product family-> Dough, Cheese, Souse etc
    - Then you can make all variants of products follow those interfaces
        ~ We want to have different ingredients-> ThinCrustDough, CheeseBurstDough, ReggianoCheese etc
    - The next move is to declare the Abstract Factory—an interface with a list of creation methods for all products that
     are part of the product family
        ~ we want to create dough, cheese etc, we can create methods for the same
    - Implement the factory interface for different location, each location can have a specific ingredient.

    The below diagram might be a bit overwhelming, but for this example we will have
    1. An abstract pizza class with attributes as the ingredients of the pizza(dough, cheese, sause etc) and an abstract
        method prepare() which all the pizzas should override to provide their unique preparation style. For example in
        cheese pizza I don't want to create instances of vegetable ingredients. We will also have an attribute for
        ingredient factory.
    2. Create interfaces for different ingredients and their concrete implementations
    3. Create an interface for ingredient factory
    4. Create implementations for factory for different locations of stores.
    5. Subclass different pizzas like cheese pizza, clam pizza etc and implement prepare method. Inside the prepare method
    create the ingredients using the ingredient factory. This factory gives the ingredients based on the location of store.

    Our goal is to
    1. Define a store for a particular location, inside this we will instantiate a location specific ingredients
    2. Create a specific pizza('Cheese') for the location


+-------------------+     +----------------------------+
| <<interface>>     |     | <<interface>>              |
| AbstractFactory   |     | AbstractProductA           |
+-------------------+     +----------------------------+
| +createProductA() |     | +usefulFunctionA()         |
| +createProductB() |     +----------------------------+
+-------------------+                 ^
        ^                              |
        |                              |
        |                              |
+-------------------+     +----------------------------+
| ConcreteFactory1  |     | ConcreteProductA1          |
+-------------------+     +----------------------------+
| +createProductA() |---->| +usefulFunctionA()         |
| +createProductB() |     +----------------------------+
+-------------------+                 ^
        ^                              |
        |                              |
        |                              |
+-------------------+     +----------------------------+
| ConcreteFactory2  |     | ConcreteProductA2          |
+-------------------+     +----------------------------+
| +createProductA() |---->| +usefulFunctionA()         |
| +createProductB() |     +----------------------------+
+-------------------+
        ^
        |
        |
+-------------------+     +----------------------------+
| <<interface>>     |     | <<interface>>              |
| Client            |     | AbstractProductB           |
+-------------------+     +----------------------------+
| +operation()      |     | +usefulFunctionB()         |
+-------------------+     +----------------------------+
                                ^
                                |
                                |
                    +----------------------------+
                    | ConcreteProductB1          |
                    +----------------------------+
                    | +usefulFunctionB()         |
                    +----------------------------+
                                ^
                                |
                                |
                    +----------------------------+
                    | ConcreteProductB2          |
                    +----------------------------+
                    | +usefulFunctionB()         |
                    +----------------------------+


"""
from abc import ABC, abstractmethod
from typing import List

class Clam(ABC):
    pass

class Sause(ABC):
    pass

class Dough(ABC):
    pass

class Cheese(ABC):
    pass

class Vegetable(ABC):
    pass


class Pizza:
    name: str
    dough: Dough
    cheese: Cheese
    sause: Sause
    vegetable: List[Vegetable]
    clam: Clam

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    def cut(self):
        print("Cutting Pizza")

    def box(self):
        print("Packing pizza")


class VeggiesA(Vegetable):
    pass

class VeggiesB(Vegetable):
    pass

class DoughA(Dough):
    pass

class DoughB(Dough):
    pass

class SauseA(Sause):
    pass

class SauseB(Sause):
    pass

class SauseC(Sause):
    pass

class ClamA(Clam):
    pass

class ClamB(Clam):
    pass

class CheeseA(Cheese):
    pass

class CheeseB(Cheese):
    pass


class PizzaIngredientFactory(ABC):
    @abstractmethod
    def get_dough(self):
        pass

    def get_clam(self):
        pass

    def get_sause(self):
        pass

class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def get_dough(self):
        print('Using DoughA')
        return DoughA()

    def get_clam(self):
        print('Using ClamB')
        return ClamB()
    
    def get_cheese(self):
        print('Using CheeseB')
        return CheeseB()

    def get_sause(self):
        print('Using SauseC')
        return SauseC()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def get_dough(self):
        print('Using DoughB')
        return DoughB()

    def get_clam(self):
        print('Using ClamA')
        return ClamA()

    def get_cheese(self):
        print('Using CheeseA')
        return CheeseA()

    def get_sause(self):
        print('Using SauseA')
        return SauseA()

    def get_veggies(self):
        print('Using VeggieA and VeggieB')
        return [VeggiesA(), VeggiesB()]

class CheesePizza(Pizza):
    pizza_ingredient_factory: PizzaIngredientFactory

    def __init__(self, pizza_ingredient_factory):
        self.pizza_ingredient_factory = pizza_ingredient_factory

    def prepare(self):
        self.dough = self.pizza_ingredient_factory.get_dough()
        self.cheese = self.pizza_ingredient_factory.get_cheese()
        self.sause = self.pizza_ingredient_factory.get_sause()

    def bake(self):
        print('Baking Cheese Pizza will take 20 minutes')


class ClamPizza(Pizza):
    pizza_ingredient_factory: PizzaIngredientFactory

    def __init__(self, pizza_ingredient_factory):
        self.pizza_ingredient_factory = pizza_ingredient_factory

    def prepare(self):
        self.dough = self.pizza_ingredient_factory.get_dough()
        self.cheese = self.pizza_ingredient_factory.get_cheese()
        self.sause = self.pizza_ingredient_factory.get_sause()
        self.clam = self.pizza_ingredient_factory.get_clam()


class PizzaStore(ABC):
    pizza: Pizza = None
    ingredient_factory: PizzaIngredientFactory = None

    def order_pizza(self, pizza_type):
        self.create_pizza(pizza_type)
        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()


    @abstractmethod
    def create_pizza(self, pizza_type):
        pass


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        self.ingredient_factory=NYPizzaIngredientFactory()
        if pizza_type=='Cheese':
            self.pizza = CheesePizza(self.ingredient_factory)
        elif pizza_type=='Clam':
            self.pizza = ClamPizza(self.ingredient_factory)



class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        self.ingredient_factory=ChicagoPizzaIngredientFactory()
        if pizza_type=='Cheese':
            self.pizza = CheesePizza(self.ingredient_factory)
        elif pizza_type=='Clam':
            self.pizza = ClamPizza(self.ingredient_factory)

if __name__ == '__main__':
    ny_pizza_store = NYPizzaStore()
    ny_pizza_store.order_pizza('Cheese')
    print('################################')
    ny_pizza_store.order_pizza('Clam')
    print("""
        ////////////////////////////////
    """)

    chicago_pizza_store = ChicagoPizzaStore()
    chicago_pizza_store.order_pizza('Clam')
