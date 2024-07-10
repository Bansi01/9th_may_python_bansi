#Write a python program to get the Fibonacci number of the given number. 

def fibonacci(n):
    if n <= 0:
     return "Input should be positive number"
    elif n == 1:
     return 0
    elif n == 2:
     return 1
    else:
      a,b = b; a+b
      return b 
num  = int(input("Enter a number:"))
print(f"The fibonacci number of{num} is {fibonacci(num)}")