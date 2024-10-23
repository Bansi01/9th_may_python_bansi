#When is the finally block executed?

#The finally block in a try-except-finally statement in Python is always executed, regardless of whether an exception was raised or not. It is typically used to release resources, close files, or perform any necessary cleanup.

try:
    # Code that might raise an exception
    x = 5 / 0
except ZeroDivisionError:
    # Handle the exception
    print("Cannot divide by zero!")
finally:
    # This block is always executed
    print("Finally block executed")