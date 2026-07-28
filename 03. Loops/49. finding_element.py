name = "Sohaib"
to_find = "o"
i = 0

while i < len(name):
    if to_find == name[i]:
        print(to_find,"found at index",i)
        break
    else:
        print("Still Searching ....")
        
    i += 1
else:
    print(to_find,"Not Found")

