#Write a python program to add'ing' at the end of the given string (Length should be at least 3), If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

def add_suffix(s):
    if len(s) < 3:
        return s
    elif s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'
    
string = input("Enter a string:")
result = add_suffix(string)

print("Result: ", result)