#Write a python program to get a string if its length is a multiple of 4.
def strings_muktiple_of_4(strings):
    return [s for s in strings if len(s) % 4 == 0]

strings = input("Enter a list of strings(space-separated):").split()
result = strings_muktiple_of_4(strings)

print("Strings with length multiple of 4:", result)