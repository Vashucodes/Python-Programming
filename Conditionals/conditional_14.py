ch = "aeiouAEIOU"

user = input("Enter the letter: ")

if len(user) != 1 or not user.isalpha():
    print("Please enter a single alphabet.")
elif user in ch:
    print("Vowel")
else:
    print("Consonant")