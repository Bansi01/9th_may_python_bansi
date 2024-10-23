#When will the else part of try-except-else be executed?

try:
    # Code that might raise an exception
    x = 5 / 1
except ZeroDivisionError:
    # Handle the exception
    print("Cannot divide by zero!")
else:
    # Code to be executed if no exception is raised
    print("Division successful:", x)