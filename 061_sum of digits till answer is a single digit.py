# Challenge 1: The Digit Sum ReductionWrite a program that takes a positive integer and calculates the sum of its digits. If the resulting sum has more than one digit, continue repeating the process until you get a single-digit number.Example Input: 9875 Process:$9 + 8 + 7 + 5 = 29$ (more than one digit, so repeat)$2 + 9 = 11$ (more than one digit, so repeat)$1 + 1 = 2$ (single digit, stop here)Expected Output: 2Hint: You will likely need a while loop on the outside to check the size of the number, and a for loop on the inside to iterate through the digits.


num = input("Enter any number: ") #9875
sum = 0
while len(num) != 1:
    for i in num:
        x = int(i)
        sum += x
    
    num = str(sum)
    sum = 0

print(num)
    

