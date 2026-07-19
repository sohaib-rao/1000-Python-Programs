messy_tuple = (1, 2, 2, 3, 4, 4, 5, 5, 5)

cleaned_tuple = tuple(set(messy_tuple))
print("Cleaned tuple:", cleaned_tuple)