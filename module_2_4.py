numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

#Способ 1
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

print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')

#Способ 2:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for number in numbers:
    is_prime = True
    
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break
    
    if is_prime:
        if number > 1:
            primes.append(number)
    else:
        not_primes.append(number)

print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')

