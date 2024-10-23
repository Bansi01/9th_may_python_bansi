#Write a Python program to copy the contents of a file to another file.

def copy_file_contents(source_file_name, destination_file_name):
    """
    Copy the contents of a file to another file.

    Args:
        source_file_name (str): The name of the source file.
        destination_file_name (str): The name of the destination file.
    """
    try:
        with open(source_file_name, "r") as source_file:
            with open(destination_file_name, "w") as destination_file:
                destination_file.write(source_file.read())
        print(f"Contents of {source_file_name} copied to {destination_file_name} successfully.")
    except FileNotFoundError:
        print(f"The file {source_file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    source_file_name = "source.txt"
    destination_file_name = "destination.txt"

    copy_file_contents(source_file_name, destination_file_name)


if __name__ == "__main__":
    main()