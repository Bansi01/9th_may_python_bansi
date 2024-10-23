# What is File function in python? What is keywords to create and write file.

The key function for working with files in Python is the open() function. The open() function takes two parameters; filename, and mode. There are four different methods (modes) for opening a file: "r" - Read - Default value. Opens a file for reading, error if the file does not exist.

In Python, you use the open() function with one of the following options – "x" or "w" – to create a new file:

"x" – Create: this command will create a new file if and only if there is no file already in existence with that name or else it will return an error.

To write : ('w’): This mode opens the file for writing only. The data in existing files are modified and overwritten. The start of the file is where the handle is located. If the file does not already exist in the folder, a new one gets created.
