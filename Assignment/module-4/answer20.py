#Write python program that user to enter only odd numbers, else will raise an exception.

class InvalidInputError(Exception):
    """Custom exception for invalid input"""
    pass

def get_odd_number():
    while True:
        try:
            num = int(input("Enter an odd number: "))
            if num % 2 == 0:
                raise InvalidInputError("Only odd numbers are allowed")
            return num
        except InvalidInputError as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    try:
        odd_num = get_odd_number()
        print(f"You entered an odd number: {odd_num}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()