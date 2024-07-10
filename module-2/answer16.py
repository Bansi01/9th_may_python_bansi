#Write a python program to get a single string from two given strings,separated by a space and swap the first two characters of the string.
def swap_first_two_chars(s1,s2):
    combined_string = s1 + " "+ s2
    if len(combined_string) >= 2:
        swapped_string = combined_string[1] + combined_string[0] + combined_string[2 :]
    else:
        swapped_string = combined_string
        return swapped_string
    
s1 = input("Enter first string:")
s2 = input("Enter secong string:")

result = swap_first_two_chars(s1, s2)

print("Result:", result)