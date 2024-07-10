#Write a python program to sum of the first n positive integers.
def sum_of_n(n): 
    return n * (n + 1) // 2
n = int(input("Enter a positive integer:"))
result = sum_of_n(n)
print(f"Sum of the first {n} positive integers: {result}")