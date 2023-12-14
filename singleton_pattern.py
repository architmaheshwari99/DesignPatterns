"""
 The Singleton Pattern ensures a class has only one instance, and provides a global point of access to it.
 We want the Singleton class to return the same instance even if there is multiple instantiation.

 In languages like Java where there are multiple threads running we can use `synchronized` keyword so that multiple
 objects are not instantiated in different threads. But the synchronization keyword add an additional overhead to a
 multiple 100x. 
"""

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Singleton:
    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

instance1 = Singleton()
instance2 = Singleton()

print(instance1 == instance2)