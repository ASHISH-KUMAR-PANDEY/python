def semiprimes(n):
    all_semiprimes = [i for i in range(4,n) if check_semi(i)]
    not_squares = [i for i in all_semiprimes if i**0.5%1]
    return all_semiprimes, not_squares

def check_semi(n, i=2):
    factors = []
    while i <= n:
        while not n%i:
            factors.append(i)
            n //= i
        i += 1
    return True if len(set(factors)) <= 2 and len(factors) == 2 else False
