base = 7
exponent = 3
modulus = 10
# pow(base, exponent, modulus) is much faster than (base ** exponent) % modulus
result = pow(base, exponent, modulus)
print(f"The secure result of {base}^{exponent} % {modulus} is: {result}")