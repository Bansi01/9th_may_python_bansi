#Write a python program to find the longest words.

def find_longest_words(file_name):
    """
    Find the longest words in a file.

    Args:
        file_name (str): The name of the file.

    Returns:
        list: A list of the longest words.
    """
    try:
        with open(file_name, "r") as file:
            words = file.read().split()
            max_length = max(len(word) for word in words)
            longest_words = [word for word in words if len(word) == max_length]
            return longest_words
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        return []


def main():
    file_name = "example.txt"

    longest_words = find_longest_words(file_name)
    print(f"The longest words in {file_name} are: {longest_words}")


if __name__ == "__main__":
    main()