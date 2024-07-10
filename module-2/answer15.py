#Wnrite a python program to count occurences of a substring in a string.
def count_substring(string, substring):
    return string.count(substring)
string = input("Enter a substring:")
substring = input("Enter the substribg:")
count = count_substring(string, substring)

print(f"The substring '{substring}' appears {count} times in the string.")