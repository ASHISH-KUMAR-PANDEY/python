def prime_factors(num):
    res = []
    while not num % 2:
        num //= 2
        res += [2]
    divisor = 3
    while num > 1:
        while not num % divisor:
            num //= divisor
            res += [divisor]
        divisor += 2
    return res


def smallest(n):
    primes = dict()
    all_primes = set()
    for i in range(2, n + 1):
        i_primes = prime_factors(i)
        primes[i] = i_primes
        all_primes.update(i_primes)
    primes_occurrence = dict()
    for p in all_primes:
        primes_occurrence[p] = 0
    for p in primes_occurrence:
        for key, lst_primes in primes.items():
            n_occurrence = lst_primes.count(p)
            if n_occurrence > primes_occurrence[p]:
                primes_occurrence[p] = n_occurrence
    lcm = 1
    for p in primes_occurrence:
        lcm *= p ** primes_occurrence[p]
    return lcm
