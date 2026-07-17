lst = [1,2,3,4,5]
d = 2
lst[:] = lst[d:] + lst[:d]
print(lst)