"""
    - Strategy Pattern is used to encapsulate behaviours and swap them at runtime
    This helps in separation of behaviour(logic) and enables limited scope of testing.
    - Strategy pattern relies on composition
    - Separation of code which stays the same and which changes

    How to use this pattern
    - Identify the behaviours that can be encapsulated and you want them swappable
    Ex: Different payment options, Different validations based on conditions
    Here payment and validations are behaviours which vary for different use case and scenarios

    - Define interface that represent the behaviour and define appropriate methods
        - we should program to interface not the implementation, this enables us to add new behaviours separately
            instead of adding in the implementation

    - Implement concrete classes for different behaviours

    Why use inheritance over composition? We could have used inheritance to define the methods and could create sub-classes
    - Every subclass would have inherited all the methods which might not be relevant, for example CreditCards will have
    an option to convert the transaction to an EMI which other modes might not have. In this case we would have to override
    and set the method to return NotImplemented() explicitly. => Maintenance is difficult here
"""
from abc import ABC, abstractmethod
from enum import Enum


class PaymentType(Enum):
    CreditCard = "Credit Card"
    DebitCard = "Debit Card"


class PaymentProcessor:
    """
        Violations
        - Open Closed Principle: Everytime we have to add a new method of payment we will have to change the implementation
        - Program to interface rather than implementation

    """
    def __init__(self):
        self._payment_type = None

    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value

    def process_payment(self, amount):
        if self.payment_type == PaymentType.CreditCard:
            print(f'Process using credit card {amount}')
        elif self.payment_type == PaymentType.DebitCard:
            print(f'Process using Debit card {amount}')
        else:
            print('Illegal Method')


# Improved Code

class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f'Process using credit card {amount}')

class DebitCardProcessPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f'Process using debit card {amount}')

class CryptoCureencyProcessPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f'Process using crypto wallet {amount}')

class ImprovedPaymentProcessor:
    """
       Things to keep in mind
       - Keep the interface simple as we don't want to change interface very frequently
       - Place the state behaviour in the concrete strategy class
       - Use dependency injection to pass the concrete strategy in context class rather than creating it inside the same
    """
    _payment_type: PaymentStrategy

    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value

    def process_payment(self, amount):
        self._payment_type.process_payment(amount)


"""
    A more detailed example for strategy pattern
"""

class KicksBehaviour(ABC):

    @abstractmethod
    def kick(self):
        pass

class PowerKick(KicksBehaviour):
    def kick(self):
        print('Power Kick')

class SlideKick(KicksBehaviour):
    def kick(self):
        print('Slide Kick')


class JumpBehaviour(ABC):
    @abstractmethod
    def jump(self):
        pass

class HighJump(JumpBehaviour):
    def jump(self):
        print('High Jump')



class Fighter(ABC):
    kick_behaviour: KicksBehaviour
    jump_behaviour: JumpBehaviour

    def __init__(self, kick_behaviour, jump_behaviour):
        self.kick_behaviour = kick_behaviour
        self.jump_behaviour = jump_behaviour

    def punch(self):
        print('Default Punch')

    def kick(self):
        self.kick_behaviour.kick()

    def jump(self):
        self.jump_behaviour.jump()

    def roll(self):
        print('Default Roll')

    def set_kick_behaviour(self, new_kick_behaviour):
        self.kick_behaviour = new_kick_behaviour

    def set_jump_behaviour(self, new_jump_behaviour):
        self.jump_behaviour = new_jump_behaviour

class Eddy(Fighter):
    def __init__(self, kick_behaviour, jump_behaviour):
        super().__init__(kick_behaviour, jump_behaviour)

    def roll(self):
        print('Style Roll')

    def punch(self):
        print('Slow Punch')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    payment_processor = PaymentProcessor()
    payment_processor.payment_type = PaymentType.CreditCard
    payment_processor.process_payment(100)

    # Improved Code
    print()
    print('>>>>>Improved Flow')
    payment_processor = ImprovedPaymentProcessor()
    payment_processor.payment_type = CreditCardProcessPayment()
    payment_processor.payment_type.process_payment(100)

    payment_processor.payment_type = CryptoCureencyProcessPayment()
    payment_processor.payment_type.process_payment(100)

    print()
    print('>>>>>Fighters example')

    eddy_fighter = Eddy(SlideKick(), HighJump())
    eddy_fighter.kick()
    eddy_fighter.punch()
    eddy_fighter.roll()
