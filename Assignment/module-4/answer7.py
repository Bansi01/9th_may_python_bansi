#Write a Python program to read a file line by line store it into a variable.
def read_file_line_by_line(file_name):
    """
    Read a file line by line and store it into a variable.

    Args:
        file_name (str): The name of the file.
    """
    try:
        with open(file_name, "r") as file:
            for line in file:
                line_variable = line.strip()
                print(f"Line: {line_variable}")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")


def main():
    file_name = "example.txt"

    read_file_line_by_line(file_name)


if __name__ == "__main__":
    main()