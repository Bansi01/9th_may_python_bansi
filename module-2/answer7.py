# Write python program to find whether to find whether the given number is even or odd, print out appropriate message to the user.

num = int(input("Enter the number:"))

if (num % 2) == 0:
    print("{0} is even" .format(num))

else:
    print("{0} is odd".format(num))