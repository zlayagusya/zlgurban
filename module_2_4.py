numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
n = 0
primes = []
not_primes = []  
i = 0
for i in range(len(numbers)):
    is_prime = True
    #    k = 0
    n = numbers[i]
    if n < 2:
        print(n, '- не простое и не сложное число')
        continue
    else:
        f = n ** (1 / 2)
    for a in range(2, int(f + 1)):
        if n % a == 0:
            is_prime = False
            break
    if not (is_prime):
        not_primes.append(n)
    else:
        primes.append(n)
is_prime = True
print('Простые числа ', primes)
print('Составные числа', not_primes)