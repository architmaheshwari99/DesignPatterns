"""
 The Command Pattern allows you to decouple the requester of an action from the object
 that actually performs the action. A command object encapsulates a request
 to do something (like turn on a light) on a specific object (say, the living room light object)

 A command object encapsulates a request by binding together a set of actions on a specific
 receiver. To achieve this, it packages the actions and the receiver up into an object that
 exposes just one method, execute(). When called, execute() causes the actions to be invoked
 on the receiver.

 +-----------------------------------+
|            <<Interface>>          |
|              Command              |
|-----------------------------------|
| + execute(): void                 |
+-----------------------------------+
         ^
         | Implements
         |
+----------------------+      +------------------------+
|    ConcreteCommand   |      |        Receiver        |
|----------------------|      |------------------------|
| # receiver: Receiver |      |                        |
|----------------------|      | + action(): void       |
| + execute(): void    |      +------------------------+
+----------------------+                 ^
         ^                               |
         | Uses                          | Uses
+----------------------+                 |
|       Invoker        |-----------------+
|----------------------|
| - command: Command   |
|----------------------|
| + setCommand(c: Command): void |
| + executeCommand(): void      |
+----------------------+

+----------------------+
|        Client        |
|----------------------|
|                      |
+----------------------+

"""
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Light:
    def __init__(self):
        self.state = False

    def on(self):
        print("Light turned on")
        self.state = True


class GarageDoor:
    def __init__(self):
        pass

    def up(self):
        pass


class LightCommand(Command):
    light: Light

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()


class GarageDoorOpener(Command):
    garage_door: GarageDoor

    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()
        self.garage_door.stop()
        self.garage_door.light_on()
        self.garage_door.down()
        self.garage_door.light_off()

class SimpleRemoteControl:
    slot1: Command

    def set_command(self, command):
        self.slot1 = command

    def button_was_pressed(self):
        self.slot1.execute()


if __name__ == "__main__":
    command = LightCommand(Light())
    remote = SimpleRemoteControl()
    remote.set_command(command)

    remote.button_was_pressed()
