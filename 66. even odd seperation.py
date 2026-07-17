nums = [2,6,4,7,8,4,8,3,1,9,5]
even, odd = [], []
for n in nums:
    if n % 2 == 0: 
        even.append(n)
    else: 
        odd.append(n)
        
print("Even:", even, "Odd:", odd)