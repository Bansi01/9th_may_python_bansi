# Write a python program that swap two number with temp variable and without temp variable?

def swap_with_temp(a,b):
    temp = a
    a = b
    b = temp
    return a,b
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

num1,num2 = swap_with_temp(num1, num2)
print(f"SWapped numbers:{num1},{num2}")

#Without temp variable:

def swap_without_temp(a,b):
    a = a + b
    b = a - b
    a = a - b
    return a,b 

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

num1,num2 = swap_without_temp(num1, num2)
print(f"SWapped numbers:{num1},{num2}")