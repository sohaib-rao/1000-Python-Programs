def reverse_str(s):
    return s if len(s) == 0 else reverse_str(s[1:]) + s[0]
print(reverse_str("hello"))