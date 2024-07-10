#Write a python program to sum of three given integers . However,if two values are equal sum will be zero.

def sum_three(a,b,c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c
    
num1 = (input("Enter first number:"))
num2 = (input("Enter secong number:"))
num3 = (input("Enter third number:"))

result = sum_three(num1, num2, num3)

print(f"Sum of three numbers:{result}")