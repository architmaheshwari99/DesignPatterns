"""
 The Template Method Pattern defines the skeleton of an algorithm in a method, deferring some steps to subclasses.
 Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm’s structure.
 Check the prepare_recipe method

What’s a template?
It’s a method that defines an
algorithm as a set of steps. One or more of these steps is defined to be abstract and implemented by a subclass


The Hollywood Principle
Don’t call us, we’ll call you

The Hollywood principle gives us a way to prevent “dependency rot.” Dependency rot happens when you have high-level
components depending on low-level components depending on high-level components and so on.

With the Hollywood Principle, we allow low-level components to hook themselves into a system,
but the high-level components determine when they are needed
"""

from abc import ABC, abstractmethod


class Coffee:
    def prepare_coffee(self):
        self.boil_water()
        self.brew_coffee_grinds()
        self.pour_in_cup()
        self.add_sugar_and_milk()

    def boil_water(self):
        print('Boiling water')

    def brew_coffee_grinds(self):
        print('brewing')

    def pour_in_cup(self):
        print('pouring')

    def add_sugar_and_milk(self):
        print('Adding sugar and milk')


class Tea:
    def prepare_coffee(self):
        self.boil_water()
        self.steep_tea_bag()
        self.pour_in_cup()
        self.add_lemon()

    def boil_water(self):
        print('Boiling water')

    def pour_in_cup(self):
        print('pouring')

    def add_lemon(self):
        print('Adding lemon')

    def steep_tea_bag(self):
        print('steep tea bag')


class CaffeineBeverage(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiment()


    def boil_water(self):
        print('Boiling water')

    def pour_in_cup(self):
        print('pouring')

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiment(self):
        pass

    def customer_wants_condiments(self):
        # To use the hook, we override it in our subclass
        return True


class CoffeeImp(CaffeineBeverage):
    def brew(self):
        print('adding coffee')

    def add_condiment(self):
        print('Adding sugar and milk')

    def customer_wants_condiments(self):
        answer = input('Do you need condiments')
        if answer == 'yes':
            return True
        return False


class TeaImp(CaffeineBeverage):
    def brew(self):
        print('steep tea bag')

    def add_condiment(self):
        print('Adding lemon')


if __name__ == '__main__':
    tea = CoffeeImp()
    tea.prepare_recipe()
