
# notebook.py (main module)

import os
import logging

# Create a log file
logging.basicConfig(filename='notebook.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def display_menu():
    print("E-Note Book Console Application")
    print("-------------------------------")
    print("1. Generate Note")
    print("2. View Notes")
    print("3. Exit")
    print("-------------------------------")

def generate_note():
    note_title = input("Enter note title: ")
    note_content = input("Enter note content: ")
    with open("notes.txt", "a") as f:
        f.write(f"{note_title}\n{note_content}\n\n")
    logging.info(f"Note '{note_title}' generated successfully")
    print("Note generated successfully!")

def view_notes():
    if os.path.exists("notes.txt"):
        with open("notes.txt", "r") as f:
            notes = f.read()
            print(notes)
    else:
        print("No notes available")
    logging.info("Notes viewed successfully")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            generate_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            logging.info("Application exited successfully")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()