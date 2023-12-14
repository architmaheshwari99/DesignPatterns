"""
    Design a slot based remote control
    Implement undo functionality, we can also implement a Double Linked List to store undo history

"""

from abc import ABC, abstractmethod
from typing import List


class Light:
    def __init__(self, description):
        self.description = description

    def on(self):
        print(f"{self} light turned on")

    def off(self):
        print(f"{self} light turned off")

    def __str__(self):
        return self.description


class Door:
    def __init__(self, description):
        self.description = description

    def open(self):
        print(f"{self} door opened")

    def close(self):
        print(f"{self} door closed")

    def __str__(self):
        return self.description


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class LightOnCommand(Command):
    light: Light

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    light: Light

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class GarageEntryCommand(Command):
    light: Light
    door: Door

    def __init__(self, light: Light, door: Door):
        self.light = light
        self.door = door

    def execute(self):
        self.light.on()
        self.door.open()

    def undo(self):
        self.door.close()
        self.light.off()

class GarageExitCommand(Command):
    light: Light
    door: Door

    def __init__(self, light: Light, door: Door):
        self.light = light
        self.door = door

    def execute(self):
        self.door.close()
        self.light.off()

    def undo(self):
        self.light.on()
        self.door.open()


class NoCommand(Command):
    def execute(self):
        return None

    def undo(self):
        return None


class RemoteControl:
    on_commands: List[Command]
    off_commands: List[Command]
    undo_command: Command

    def __init__(self):
        self.on_commands = []
        self.off_commands = []
        command = NoCommand()
        for i in range(7):
            self.on_commands.append(command)
            self.off_commands.append(command)

    def set_command(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_pressed(self, slot):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_pressed(self, slot):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def undo_button_pressed(self):
        self.undo_command.undo()


if __name__ == "__main__":
    rc = RemoteControl()
    living_room_light = Light('Living Room')
    rc.set_command(0, LightOnCommand(living_room_light), LightOffCommand(living_room_light))
    rc.on_button_pressed(0)
    rc.off_button_pressed(0)
    print('#####')
    garage_light = Light('Garage')
    garage_door = Door('Garage')
    rc.set_command(1, GarageEntryCommand(garage_light, garage_door), GarageExitCommand(garage_light, garage_door))
    rc.on_button_pressed(1)
    rc.off_button_pressed(1)
    print('#####')
    rc.undo_button_pressed()
