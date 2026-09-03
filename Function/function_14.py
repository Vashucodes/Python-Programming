def is_palindrome(n):
    original = n
    rev = 0
    while n != 0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10 

    if original == rev :
        return True
    else:
        return False


n = int(input("Enter the number:"))

print(is_palindrome(n))