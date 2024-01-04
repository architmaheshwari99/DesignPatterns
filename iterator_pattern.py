"""

The Iterator Pattern provides a way to access the elements of an aggregate object sequentially without
exposing its underlying representation.

We have 2 menus, PanCakeHouseMenu and DinerMenu. Both menus have an underlying logic to store the details of the dishes.
Because of this the client has to know about the underlying structure of the storage of menu for each menu which beats the
purpose of encapsulation.

Idea is to extract the logic of traversal of internal datastructure in the form of an iterator


>>>>>
We have duplicate code: the printMenu() method needs two separate loops to iterate over the two different kinds of menus
And if we added a third menu, we’d have yet another loop.

The first thing you need to know about the Iterator Pattern is that it relies on an interface called Iterator.
Here’s one possible Iterator interface:
-> has_next()
-> next()


with the two implementations of Menus. But the effect of using iterators in your design is just as important:
you'll have a uniform way of accessing the elements of all your aggregate objects

Iterator Pattern takes the responsibility of traversing elements and gives that responsibility to the iterator object
(PanCakeHouseMenuIterator), not the aggregate object(PanCakeHouseMenu).
This not only keeps the aggregate interface and implementation simpler

Cohesion refers to the degree to which the elements inside a module or a class belong together.
It's a measure of how closely related and focused the responsibilities of a module or class are.


+------------------+         +---------------------+
| <<Interface>>    |         | <<Interface>>       |
| Aggregate        |<------->| Iterator            |
+------------------+         +---------------------+
| +createIterator()|         | +first()            |
+------------------+         | +next()             |
      ^                      | +isDone()           |
      |                      | +currentItem()      |
      |                      +---------------------+
+------------------+                  ^
| ConcreteAggregate|                  |
+------------------+                  |
| +createIterator()|                  |
+------------------+         +---------------------+
                            | ConcreteIterator     |
                            +---------------------+
                            | +first()            |
                            | +next()             |
                            | +isDone()           |
                            | +currentItem()      |
                            +---------------------+


"""

from abc import abstractmethod, ABC
from datetime import datetime
from typing import Optional, List


class MenuItem:
    def __init__(self, name: str, description: str, veg: bool, price: float):
        self.name = name
        self.description = description
        self.veg = veg
        self.price = price

    def __str__(self):
        return f"{self.name}, {self.description} @ {self.price}"


class PanCakeHouseMenu:
    def __init__(self):
        self.menu_items: List[MenuItem] = []

        self.add_item('Item 1', 'Very tasty samosa 1', True, 2.99)
        self.add_item('Item 2', 'Very tasty samosa 2', True, 1.99)
        self.add_item('Item 3', 'Very tasty samosa 3', True, 4.99)

    def add_item(self, name: str, description: str, veg: bool, price: float) -> None:
        self.menu_items.append(MenuItem(name, description, veg, price))

    def get_menu_items(self) -> List[MenuItem]:
        return self.menu_items


class DinerMenu:
    def __init__(self):
        self.menu_items: List[List[MenuItem]] = []

        self.add_item('Item 1', 'Very tasty Dal 1', True, 12.99)
        self.add_item('Item 2', 'Very tasty Dal 2', True, 21.99)
        self.add_item('Item 3', 'Very tasty Dal 3', True, 9.99)

    def add_item(self, name: str, description: str, veg: bool, price: float):
        self.menu_items.append([MenuItem(name, description, veg, price)])

    def get_menu_items(self) -> List[List[MenuItem]]:
        return self.menu_items


class CombinedMenu1:
    def print_menu(self):
        diner_menu = DinerMenu()
        diner_menu_list = diner_menu.get_menu_items()

        # Different ways of iterating over different menus
        for item in diner_menu_list:
            print(item[0])

        pancake_menu = PanCakeHouseMenu()
        pancake_menu_list = pancake_menu.get_menu_items()

        for item in pancake_menu_list:
            print(item)


class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass


class DinerMenuIterator(Iterator):
    def __init__(self, items):
        self.items = items
        self.pos = 0

    def next(self):
        menu_item = self.items[self.pos]
        self.pos += 1
        return menu_item[0]

    def has_next(self) -> bool:
        if self.pos >= len(self.items) or self.items[self.pos] is None:
            return False
        return True


class PanCakeHouseMenuIterator(Iterator):
    def __init__(self, items):
        self.items = items
        self.pos = 0

    def next(self):
        menu_item = self.items[self.pos]
        self.pos += 1
        return menu_item

    def has_next(self):
        if self.pos >= len(self.items) or self.items[self.pos] is None:
            return False
        return True


class AlternateMenuIterator(Iterator):
    def __init__(self, items):
        current_datetime = datetime.now()

        # Get the day of the week as an integer (Monday is 0, Sunday is 6)
        day_of_week_number = current_datetime.weekday()
        self.items = items
        self.pos = day_of_week_number % 2

    def next(self):
        menu_item = self.items[self.pos]
        self.pos += 2
        return menu_item

    def has_next(self):
        if self.pos >= len(self.items) or self.items[self.pos] is None:
            return False
        return True


class Menu(ABC):
    @abstractmethod
    def get_menu_items_itr(self) -> Iterator:
        pass


class DinerMenuImp(Menu):
    def __init__(self):
        self.menu_items = []

        self.add_item('Item 1', 'Very tasty Dal 1', True, 12.99)
        self.add_item('Item 2', 'Very tasty Dal 2', True, 21.99)
        self.add_item('Item 3', 'Very tasty Dal 3', True, 9.99)

    def add_item(self, name: str, description: str, veg: bool, price: float):
        self.menu_items.append([MenuItem(name, description, veg, price)])

    def get_menu_items_itr(self) -> DinerMenuIterator:
        return DinerMenuIterator(self.menu_items)


class PanCakeHouseMenuImp(Menu):
    def __init__(self):
        self.menu_items = []

        self.add_item('Item 1', 'Very tasty samosa 1', True, 2.99)
        self.add_item('Item 2', 'Very tasty samosa 2', True, 1.99)
        self.add_item('Item 3', 'Very tasty samosa 3', True, 4.99)

    def add_item(self, name: str, description: str, veg: bool, price: float):
        self.menu_items.append(MenuItem(name, description, veg, price))

    def get_menu_items_itr(self) -> PanCakeHouseMenuIterator:
        return PanCakeHouseMenuIterator(self.menu_items)


class CombinedMenu2:
    def __init__(self, diner_menu: Menu, pancake_menu: Menu):
        self.diner_menu = diner_menu
        self.pancake_menu = pancake_menu
        self.diner_menu_list: Optional[Iterator] = None
        self.pancake_menu_list: Optional[Iterator] = None

    def print_menu(self):
        self.diner_menu_list = self.diner_menu.get_menu_items_itr()
        self.pancake_menu_list = self.pancake_menu.get_menu_items_itr()
        self.print_list(self.diner_menu_list)
        self.print_list(self.pancake_menu_list)

    @staticmethod
    def print_list(menu_list):
        while menu_list.has_next():
            print(menu_list.next())


class CombinedMenu3:
    def __init__(self, menu: List[Menu]):
        self.menus = menu

    def print_menu(self):
        for menus in self.menus:
            menu_itr = menus.get_menu_items_itr()
            self.print_list(menu_itr)

    @staticmethod
    def print_list(menu_list):
        while menu_list.has_next():
            print(menu_list.next())


if __name__ == "__main__":
    CombinedMenu1().print_menu()
    print(">>>> Improved")

    CombinedMenu2(DinerMenuImp(), PanCakeHouseMenuImp()).print_menu()
    """
    Those three calls to printMenu() are looking kind of ugly.
    every time we add a new menu we are going to have to open up
    the Waitress implementation and add more code. Can you say “violating the Open Closed Principle?”
    """
    print(">>>> Improved, not calling print explicitly for all the menus")
    CombinedMenu3([DinerMenuImp(), PanCakeHouseMenuImp()]).print_menu()
