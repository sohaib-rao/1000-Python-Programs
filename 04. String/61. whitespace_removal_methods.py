messy_text = "   Hello Python!   "

print("Original with spaces:", repr(messy_text))
print("Remove both sides :", repr(messy_text.strip()))
print("Remove left side :", repr(messy_text.lstrip()))
print("Remove right side :", repr(messy_text.rstrip()))

custom_trim = "###Hello###"
print("Custom strip ('#'):", repr(custom_trim.strip('#')))
