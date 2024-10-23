#What is Instantiation in terms of OOP terminology?


'''In Object-Oriented Programming (OOP) terminology, instantiation is the process of creating an instance of a class.

In other words, instantiation is when you create a new object from a class definition. This object is called an instance of the class, and it has its own set of attributes (data) and methods (functions) that are defined by the class.'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Fido", 3)  # Instantiation!

