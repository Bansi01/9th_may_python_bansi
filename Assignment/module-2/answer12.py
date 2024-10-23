#Write the python program to calculate the lenght of the string
def string_length(s):
    return len(s)

string = input("Enter a string:")
length = string_length(string)
print(f"The length of the string is: {length}")