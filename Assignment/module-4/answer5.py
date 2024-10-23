#Write a Python program to read last n lines of a file.

def read_last_n_lines(file_name, n):
    """
    Read the last N lines of a file.

    Args:
        file_name (str): The name of the file.
        n (int): The number of lines to read.

    Returns:
        list: A list of the last N lines of the file.
    """
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            return lines[-n:]
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        return []


def main():
    file_name = "example.txt"
    n = 5

    lines = read_last_n_lines(file_name, n)
    print(f"The last {n} lines of {file_name} are:")
    for line in lines:
        print(line.strip())


if __name__ == "__main__":
    main()