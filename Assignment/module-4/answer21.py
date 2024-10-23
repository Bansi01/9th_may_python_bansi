#What are oops concepts? Is multiple inheritance supported in java

'''OOPS (Object-Oriented Programming System) concepts are the fundamental principles that define the object-oriented programming paradigm. The main OOPS concepts are:

Encapsulation: Hiding the implementation details of an object from the outside world and only exposing the necessary information through public methods.
Abstraction: Showing only the necessary information to the outside world while hiding the internal implementation details.
Inheritance: Creating a new class (subclass) that inherits the properties and behavior of an existing class (superclass).
Polymorphism: The ability of an object to take on multiple forms, depending on the context. This can be achieved through method overriding or method overloading.
Composition: Creating objects from other objects or collections of objects.


Multiple Inheritance in Java:

In Java, multiple inheritance is not supported in the classical sense. A Java class can only extend one parent class using the extends keyword. This is known as single inheritance.

However, Java does support multiple inheritance through interfaces. A Java class can implement multiple interfaces using the implements keyword. An interface is a abstract class that contains only method declarations and constants.''Multiple inheritance through interfaces'''

# Multiple inheritance in Python

class Flyable:
    def fly(self):
        print("Flying")

class Walkable:
    def walk(self):
        print("Walking")

class Bird(Flyable, Walkable):
    def __init__(self):
        pass

bird = Bird()
bird.fly()  # Output: Flying
bird.walk()  # Output: Walking