letter = input("Enter a letter: ").lower()

if len(letter) != 1 or not letter.isalpha():
    print("Please enter a single alphabet.")
elif letter in "aeiou":
    print("Vowel")
else:
    print("Consonant")

