"""
    Decorator patterns attaches additional responsibility to an object by placing these objects inside special
    wrapper objects that contain the behaviour(responsibility).

    Example: We want to design ordering system for starbucks, the main requirement is person can order a base drink
    (cappuccino, latte, tea) and add condiments(mocha, whip cream) on top of it. The add ons can be in any number, like
    we can have a cappuccino with double whip cream.

    Solution: One solution is to directly create a beverage class and define description and cost method for each of the
    possible combinations, but it will soon cause class explosion as our menu grows.

    We have a base drink and we want to compute the total cost at runtime by decorating the base drink object with
    the add ons. 
    1. Create a base abstract class/interface which defines the properties of the base drink and its add-ons (Beverage)
    2. Create concrete classes for the drinks(Latte, Cappuccino) subclassing Beverage
    3. Create a Decorator class subclassing Beverage(this is done so that the further subclasses also implements the 
        abstract methods). We will also have a composition relation from Decorator for beverage. This is done so that 
        we can do operations on the beverage object.
    4. For all the add-ons, create the concrete implementations subclassing Decorator class.

    Implementing the above satisfies the Open Close Principle as we are not modifying the base class when we want to
    add a new drink or add-on.

    Decorator pattern can be applied when we want our object to do much more than its functionality at runtime.
    Another example can be, if we have multiple communication channel and we want to notify our users in different
    combinations. Example- Slack+Email, Email, Email+push notifications etc 

    Decorator Pattern UML Diagram
------------------------------

1. Component (Interface/Abstract Class)
   |
   |   (inherits)
   |
   V
2. ConcreteComponent (Class)
   |
   |
   |  (implements/extends)
   |
   V
3. Decorator (Abstract Class)
   | <----------------------------------|
   |  (contains a reference to)         |
   |                                    |
   V                                    |
4. ConcreteDecorator1, ConcreteDecorator2, ... (Classes)
   (extend Decorator and add their own behaviors)

Note: A solid line with an arrow indicates inheritance, and a solid line with a diamond indicates composition.


"""
from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

class Latte(Beverage):
    def cost(self):
        return 12.99

    def description(self):
        return "Latte"

class Cappuccino(Beverage):
    def cost(self):
        return 10.99

    def description(self):
        return "Cappuccino"
    
class Expresso(Beverage):
    def cost(self):
        return 7.99

    def description(self):
        return "Expresso"


class Decorator(Beverage):
    beverage: Beverage

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def cost(self):
        pass

    def description(self):
        pass

class WhipCream(Decorator):
    def cost(self):
        return self.beverage.cost() + 1.99

    def description(self):
        return self.beverage.description() + " + Whipped Cream"
    
class Mocha(Decorator):
    def cost(self):
        return self.beverage.cost() + 2.99

    def description(self):
        return self.beverage.description() + " + Mocha"


class Hazelnut(Decorator):
    def cost(self):
        return self.beverage.cost() + 0.99

    def description(self):
        return self.beverage.description() + " + Hazelnut"

if __name__ == "__main__":
    beverage = Cappuccino()
    beverage = WhipCream(beverage)
    beverage = WhipCream(beverage)
    beverage = Hazelnut(beverage)
    print(beverage.cost())
    print(beverage.description())
