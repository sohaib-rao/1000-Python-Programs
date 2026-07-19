def palindrome_check(string):
    return "is palidrome" if string == string[::-1] else "not a palindrome"

print(palindrome_check("racecar"))