t = (1, 2, 3, 4, 5, 6)
even = len([x for x in t if x % 2 == 0])
odd = len([x for x in t if x % 2!= 0])
print("Even:", even, "Odd:", odd)