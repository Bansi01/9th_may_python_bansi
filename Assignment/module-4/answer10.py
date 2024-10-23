#Write a Python program to count the frequency of words in a file.

import re
from collections import Counter

def count_word_frequency(file_name):
    """
    Count the frequency of words in a file.

    Args:
        file_name (str): The name of the file.

    Returns:
        dict: A dictionary where the keys are the words and the values are their frequencies.
    """
    try:
        with open(file_name, "r") as file:
            text = file.read().lower()
            words = re.findall(r'\b\w+\b', text)
            word_frequency = Counter(words)
            return dict(word_frequency)
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        return {}


def main():
    file_name = "example.txt"

    word_frequency = count_word_frequency(file_name)
    if word_frequency:
        print("Word Frequency:")
        for word, frequency in word_frequency.items():
            print(f"{word}: {frequency}")


if __name__ == "__main__":
    main()