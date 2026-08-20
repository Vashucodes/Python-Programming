num = int(input("Enter the number:"))
original = num
reverse = 0
while num > 0:
    
    digit = num % 10 # Take the last digit
   
    reverse = reverse * 10 + digit # Add it to reverse
    num = num // 10# Remove the last digit
    
if original == reverse:
    print("Given number is palindrome")
else:
    print("Given number is not palindrome")