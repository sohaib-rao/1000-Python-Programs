# Using the step feature to skip characters
# [start:end:step] -> a step of 2 means "take every 2nd character"
alphabet = "abcdefghij"

# Start at 0, go to the end, skip by 2
every_second_letter = alphabet[::2] 

print("Original:", alphabet)
print("Every second letter:", every_second_letter)