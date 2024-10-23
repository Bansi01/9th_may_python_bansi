#Can one block of except statements handle multiple exception?

#Yes, one block of except statements can handle multiple exceptions in Python. You can specify multiple exception types in a tuple after the except keyword.

try:
    # Code that might raise an exception
    x = 5 / 0
except (ZeroDivisionError, TypeError):
    # Handle both ZeroDivisionError and TypeError
    print("An error occurred!")
