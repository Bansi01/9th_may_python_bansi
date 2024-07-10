#Write a python function that takes a list of words and returns the length of the longest one.

def longest_word_length(words):
    return max(len(word) for word in words)
words = input("Enter a listof words (space-separated):").split()
result = longest_word_length(words)

print("Length of the longest word:", result)