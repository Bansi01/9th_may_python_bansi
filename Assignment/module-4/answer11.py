#Write a Python program to write a list to a file.

def write_list_to_file(file_name, list_to_write):
    """
    Write a list to a file.

    Args:
        file_name (str): The name of the file.
        list_to_write (list): The list to write to the file.
    """
    try:
        with open(file_name, "w") as file:
            for item in list_to_write:
                file.write(str(item) + "\n")
        print(f"List written to {file_name} successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    file_name = "example.txt"
    list_to_write = [1, 2, 3, "hello", "world", 4.5, True]

    write_list_to_file(file_name, list_to_write)


if __name__ == "__main__":
    main()