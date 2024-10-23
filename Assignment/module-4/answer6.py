#Write a Python program to read a file line by line and store it into a list

def read_file_line_by_line(file_name):
    """
    Read a file line by line and store it into a list.

    Args:
        file_name (str): The name of the file.

    Returns:
        list: A list of lines from the file.
    """
    try:
        with open(file_name, "r") as file:
            lines = [line.strip() for line in file]
            return lines
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        return []


def main():
    file_name = "example.txt"

    lines = read_file_line_by_line(file_name)
    print(f"The lines from {file_name} are:")
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()