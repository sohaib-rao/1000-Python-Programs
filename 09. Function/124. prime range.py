def prime_range(start, end):
    primes = []
    for n in range(start, end + 1):
        if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1)):
            primes.append(n)
    return primes

print(prime_range(1, 100))