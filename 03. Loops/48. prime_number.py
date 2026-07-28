num = 11

for i in range(2, num):
    if num % i == 0:
        print(num,"is a Composite Number")
        break
else:
    print(num,"is a prime Number")