#Write a Python program to count the number of lines in a text file.

def count_lines(file_name):
    """
    Count the number of lines in a text file.

    Args:
        file_name (str): The name of the file.

    Returns:
        int: The number of lines in the file.
    """
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        return None


def main():
    file_name = "example.txt"

    line_count = count_lines(file_name)
    if line_count is not None:
        print(f"The file {file_name} has {line_count} lines.")


if __name__ == "__main__":
    main()