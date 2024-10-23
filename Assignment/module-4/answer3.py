#Write a Python program to append text to a file and display the text.

def append_to_file(file_name, text):
    """
    Append text to a file.

    Args:
        file_name (str): The name of the file.
        text (str): The text to be appended.
    """
    try:
        with open(file_name, "a") as file:
            file.write(text + "\n")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        with open(file_name, "w") as file:
            file.write(text + "\n")


def display_file_content(file_name):
    """
    Display the content of a file.

    Args:
        file_name (str): The name of the file.
    """
    try:
        with open(file_name, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")


def main():
    file_name = "example.txt"
    text = "This is an example text."

    append_to_file(file_name, text)
    print(f"Text appended to {file_name} successfully.")
    print("File Content:")
    display_file_content(file_name)


if __name__ == "__main__":
    main()