"""
There can be a very practical usecase where we can have nested menus. For example, A menu contains categories(consider
them as small menus) within themselves. What would be the best way to access and traverse the same


The Composite Pattern allows you to compose objects into tree structures to represent part-whole hierarchies.
Composite lets clients treat individual objects and compositions of objects uniformly.

Elements with child elements are called node
Elements without children are called leaves.

We can represent our Menu and MenuItems in a tree structure.
Menus are nodes and MenuItems are leaves.

Any menu is a “composition” because it can contain both other menus and menu items
Using a composite structure, we can apply the same operations over both composites and individual objects.
In other words, in most cases we can ignore the differences between compositions of objects and individual objects.

All components must implement the MenuComponent interface; however, because leaves and nodes have different roles
we can’t always define a default implementation for each method that makes sense.
Sometimes the best you can do is throw a runtime exception.

a component can have a pointer to a parent to make traversal of the structure easier. And, if you have a reference
to a child, and you need to delete it, you’ll need to get the parent to remove the child.
Having the parent reference makes that easier too.


MenuComponent(ABC)
- add
- remove
- get_child
- ...

Menu(MenuComponent)
attr (menu_components)


MenuItem(MenuComponent)

Iterator
MenuIterator
"""
from abc import ABC, abstractmethod
from typing import List


class MenuComponent(ABC):
    def add(self, menu_component):
        raise NotImplemented()

    def remove(self, menu_component):
        raise NotImplemented()

    def get_child(self, i):
        raise NotImplemented()

    def get_name(self):
        raise NotImplemented()

    def get_description(self):
        raise NotImplemented()

    def get_price(self):
        raise NotImplemented()

    def is_veg(self):
        raise NotImplemented()

    def _print(self):
        raise NotImplemented()


class MenuItem(MenuComponent):
    def __init__(self, name: str, description: str, vegetarian: bool, price: float):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def is_veg(self):
        return self.vegetarian

    def get_price(self):
        return self.price

    def _print(self):
        print(f"{self.name}, {self.vegetarian}, {self.price}, {self.description}")


class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


class MenuIterator(Iterator):
    def __init__(self, menu: List[MenuComponent]):
        self.position = 0
        self.menu = menu

    def next(self):
        menu_component = self.menu[self.position]
        self.position += 1
        return menu_component

    def has_next(self):
        return False if self.position >= len(self.menu) or self.menu[self.position] is None else True


class Menu(MenuComponent):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.menu_components: List[MenuComponent] = []

    def add(self, menu_component: MenuComponent):
        self.menu_components.append(menu_component)

    def remove(self, menu_component: MenuComponent):
        self.menu_components.remove(menu_component)

    def get_child(self, i):
        return self.menu_components[i]

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def _print(self):
        print(f"{self.name}, {self.description}")
        itr = MenuIterator(self.menu_components)
        while itr.has_next():
            itr.next()._print()


class Waitress:
    def __init__(self, menus):
        self.menus = menus

    def print_menu(self):
        self.menus._print()


if __name__ == "__main__":
    pancake_house_menu = Menu("pancakes", "breakfast")
    dinner_menu = Menu("Diner Menu", "Lunch")
    cafe_menu = Menu("Cafe Menu", "Dinner")
    dessert_menu = Menu("Dessert", "Dessert")

    all_menus = Menu("All Menus", "Combined menus")

    all_menus.add(pancake_house_menu)
    all_menus.add(dinner_menu)
    all_menus.add(cafe_menu)
    dessert_menu.add(MenuItem('Item 11', 'Very tasty Cake 1', True, 22.99))
    dessert_menu.add(MenuItem('Item 12', 'Very tasty Cake 2', True, 22.99))
    dinner_menu.add(MenuItem('Item 1', 'Very tasty Dal 1', True, 12.99))
    dinner_menu.add(MenuItem('Item 2', 'Very tasty Dal 2', False, 2.99))
    dinner_menu.add(dessert_menu)

    waitress = Waitress(all_menus)
    waitress.print_menu()
