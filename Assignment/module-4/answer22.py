# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

'''A class is defined using the class keyword followed by the name of the class. The class definition is typically enclosed in a block of code, which is denoted by indentation.

class ClassName:
    # class definition

    Self is a reference to the current instance of the class and is used to access variables and methods from the class. It's a convention to use the name self for the first parameter of a method, but you can use any other name if you prefer.

self is used to:

Access instance variables (data attributes) of the class.
Call other methods of the same class.'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

    def display_info(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
