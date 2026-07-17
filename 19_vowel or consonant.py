letter = 'e'.lower()

if letter in 'aeiou':
    print("It's a vowel.")
elif letter.isalpha(): # Checks if it's an actual letter, not a number or symbol
    print("It's a consonant.")
else:
    print("Invalid input.")