# Write a python program to count the number of character (character frequency in a string)

def char_frequency(s):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

string = input("Enter a string: ")
freq = char_frequency(string)
print("Character Frequency:")
for char, count in freq.items():
    print(f"{char}: {count}")



