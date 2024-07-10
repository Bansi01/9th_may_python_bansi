#Write a python program to test whether a given number a passed letter os a vowel or not.

def is_vowel(letter):
    vowels = 'aeiuAEIOU'
    if letter in vowels:
        return True
    else:
        return False
    
letter = input("Enter the letter:")
if is_vowel(letter):
    print(letter, "is a vowel")
else:
    print("Letter is not vowel")
