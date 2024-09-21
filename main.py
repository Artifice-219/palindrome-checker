def is_palindrome(str):
    if(str == str[::-1]):
        return True
    else:
        return False


str = str(input('Enter a string :'))

if(is_palindrome(str)):
    print('A palindrome')
else:
    print('Not a palindrome')