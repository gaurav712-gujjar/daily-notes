# Python Abstract Base Classes

**Category:** Python  
**Date:** 2026-08-06 (morning)

---

# Python Abstract Base Classes
Python Abstract Base Classes (ABCs) are a way to define a blueprint for other classes to follow. They allow you to create a base class that can't be instantiated on its own and is meant to be inherited by other classes. ABCs are useful when you want to provide a common interface for a group of related classes.

ABCs are used in practice when you want to define an interface or a base class that has some common methods or properties that should be implemented by all subclasses. They are particularly useful in situations where you want to ensure that all subclasses implement certain methods or properties.

For example, you can use an ABC to define a base class for a group of classes that represent different types of vehicles. The base class can have methods like `start_engine()` and `accelerate()`, which should be implemented by all subclasses.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def accelerate(self):
        print("Car accelerating")
```
