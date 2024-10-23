#Write a python program to find the first appearance of the substring 'not' and 'poor' from the given string , if 'not' follows the 'poor' replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
def replace_not_poor(s):
    poor_index = s.find('poor')
    not_index = s.find('not')

    if poor_index != -1 and not_index > poor_index:
       start = poor_index
       end = not_index + 'good' + s[end:]
    else:
        return s
    
string = input("Enter a string:")
result = replace_not_poor(string)

print("Result:", result)
