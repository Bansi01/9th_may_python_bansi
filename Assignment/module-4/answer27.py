#What is used to check whether an object o is an instance of class A?

class Animal:
    pass

class Dog(Animal):
    pass

my_dog = Dog()

print(isinstance(my_dog, Dog))  # True
print(isinstance(my_dog, Animal))  # True
print(isinstance(my_dog, str))  # False