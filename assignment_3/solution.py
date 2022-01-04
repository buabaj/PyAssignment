# print whether a string is a palindrome or not


def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return "The string is a palindrome"
    else:
        return "The string is not a palindrome"


string = input("Enter a string: ")
print(is_palindrome(string))
