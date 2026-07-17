num_to_check = 7
is_prime = True
for i in range(2, num_to_check):
    if num_to_check % i == 0:
        is_prime = False
        break
print(is_prime)