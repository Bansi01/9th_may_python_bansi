#Write a python program that will return if the two given integer values are equal of their sum or difference is 5.

def test_number5(x,y):
    # condition to check:
#1. x = y.
#2. The absolute difference between x and y is equal to 5.
#3. The sum of x and y is equal to 5.
  if x == y or abs( x - y) == 5 or ( x + y ) == 5:
    return True
  else:
        return False 

print(test_number5(7,2))
print(test_number5(3,2))
print(test_number5(27,53))
print(test_number5(2,2))
print(test_number5(4,2))
print(test_number5(7,3))
