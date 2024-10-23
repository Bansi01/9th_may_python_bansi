#How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.

'''Try Block: The try block contains the code that might raise an exception.

Except Block: The except block catches the exception raised in the try block and handles it.

Finally Block: The finally block is optional and is used to perform cleanup or release resources, regardless of whether an exception was raised or not.

eg:'''

try:
    # Code that might raise an exception
    x = 5 / 0
except ZeroDivisionError:
    # Handle the exception
    print("Cannot divide by zero!")
finally:
    # Perform cleanup or release resources
    print("Finally block executed")