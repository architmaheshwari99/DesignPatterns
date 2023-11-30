"""
    Observer pattern is a behavioural pattern, which is used to notify multiple objects
    about any event/change they have subscribed to.

    Imagine a weather station which has a real time data about the weather. If you want to get the updated data on your
    mobile, you have 2 options. First option is to poll from information from the weather station after a periodic interval
    This approach might not work as
        - We would not be sure about a correct interval between 2 polling calls
        - Imagine 1000s of devices making poll requests to the weather station server

    Another approach is that the subject tells that its state has changed and should notify about the change to the
    observers. In our case, if the data about the weather changes in weather station, we should get notified.

    Multiple observers(subscriber) can subscribe to a Subject(Observable/Publisher). They can be added and removed anytime

    Design notes
    - We should have a standard implementation for observers and observables that's why we will create interface for both
    of them and concrete implementations can be derived for both of them.
    - Each observable will have a list of observers to which it has to notify about the change in state


    +------------------+                         +------------------+
    |     Subject      |                         |     Observer     |
    +------------------+<>---------------------->|                  |
    | -observers       |                         |                  |
    | +attach(observer)|                         | +update()        |
    | +detach(observer)|                         +------------------+
    | +notify()        |                               /\
    +------------------+                               |
                                                     ---
                                                      |
                                                      |
                                     +--------------------------------+
                                     |              ConcreteObserver1  |
                                     |                                |
                                     |  +update()                     |
                                     |                                |
                                     +--------------------------------+



"""
from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    def update(self, data):
        pass

class Subject(ABC):
    def __init__(self):
        self.observers: List[Observer] = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        if observer not in self.observers:
            raise ValueError()
        self.observers.remove(observer)

    def notify(self, state):
        for observer in self.observers:
            observer.update(state)


class WeatherState:
    def __init__(self, temperature, humidity, wind_direction):
        self.temperature = temperature
        self.humidity = humidity
        self.wind_direction = wind_direction

    def __str__(self):
        return f"Temperatur is {self.temperature} `C  and humidity is {self.humidity}% and wind direction is {self.wind_direction}"


class WeatherStation(Subject):
    def __init__(self, weather_state: WeatherState):
        self.weather_state = weather_state
        super().__init__()

    def measurements_changed(self, ):
        self.notify(self.weather_state)

    def set_weather_state(self, weather_state):
        self.weather_state = weather_state
        self.measurements_changed()



class Display(ABC):
    @abstractmethod
    def display_data(self, data):
        print(data)


class MobileDisplay(Display):
    def display_data(self, data: WeatherState):
        print(data, ', Click to download the app')


class ThermometerDisplay(Display):
    def display_data(self, data: WeatherState):
        print(f"{data.temperature} `C on thermometer")


class Mobile(Observer):
    def __init__(self, display: Display):
        self.display = display

    def update(self, data):
        self.display.display_data(data)


class Thermometer(Observer):
    def __init__(self, display):
        self.display = display

    def update(self, data):
        self.display.display_data(data)


if __name__ == '__main__':
    mobile_display = MobileDisplay()
    thermometer_display = ThermometerDisplay()

    archits_mobile = Mobile(mobile_display)
    archits_thermometer = Thermometer(thermometer_display)

    weather_state = WeatherState(10, 2, 'N')
    weather_station = WeatherStation(weather_state)
    weather_station.add_observer(archits_mobile)
    weather_station.add_observer(archits_thermometer)
    weather_station.set_weather_state(weather_state)
