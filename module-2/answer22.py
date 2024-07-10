#Write a python function to insert a string in the middle of the string.
def insert_in_middle(s, insert):
    middle_index = len(s) // 2
    return s[:middle_index] + insert + s[middle_index:]
string = input("Enter a string:")
insert_string = input("Enter a string to insert:")
result = insert_in_middle(string, insert_string)

print("Result:", result)