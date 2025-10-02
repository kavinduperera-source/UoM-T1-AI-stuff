n=10
primes = []
for number in range(2, n + 1):
    is_prime = True
    for factor in range(2, int(number**0.5) + 1):
        if number % factor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)

lcm = 1
for p in primes:
    power = p
    while power*p <= n:
        power = power*p
    lcm = lcm*power

print(lcm)    
    
    
