#Write a python program to get a string made of the first 2 and the last two chars from a given string. If the string lenght is less then 2, return instead ofthe empty string.

def first_last_chars(s):
    if len(s) < 2:
        return "Empty string"
    elif len(s) == 2:
        return s + s
    else:
        return s[:2] + s[-2:]
    
string = input("Enter a string:")
result = first_last_chars(string)

print("Result: ", result)