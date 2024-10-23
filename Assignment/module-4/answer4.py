#Write a Python program to read first n lines of a file.

def read_first_n_lines(file_name, n):
    """
    Read the first N lines of a file.

    Args:
        file_name (str): The name of the file.
        n (int): The number of lines to read.

    Returns:
        list: A list of the first N lines of the file.
    """
    try:
        with open(file_name, "r") as file:
            lines = [next(file).strip() for _ in range(n)]
            return lines
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        return []
    except StopIteration:
        print(f"The file {file_name} has less than {n} lines.")
        return []


def main():
    file_name = "example.txt"
    n = 5

    lines = read_first_n_lines(file_name, n)
    print(f"The first {n} lines of {file_name} are:")
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()