#Explain Exception handling? What is an Error in Python?
try:
    # code that might raise an exception
except ExceptionType:
    # code to handle the exception

try:
    int("hello")
except ValueError:
    print("Invalid input. Please enter a valid integer.")