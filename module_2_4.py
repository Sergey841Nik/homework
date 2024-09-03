numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for number in numbers:
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                not_primes.append(number)
                break
for prime in numbers:
    if prime > 1:
        if prime not in not_primes:
            primes.append(prime)


print(primes, not_primes, sep="\n")
