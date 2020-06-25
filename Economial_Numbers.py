def prime_factors(n):
    i=0;primes=[]
    while i*i<n:
        i+=2
        while n%i==0:
            primes.append(i)
            n//=i
        if i==2:i=1
    if n>1:primes.append(n)
    return primes     

def is_economical(n):
    ln=len(str(n))
    p=prime_factors(n)
    c=[];e=0
    for i in p:
        if i not in c:
            c.append(i)
            if p.count(i)>1:
                e+=len(str(i)+str(p.count(i)))
            else:
                e+=len(str(i))
    if e==ln:
        return 'Equidigital'
    elif e<ln:
        return 'Frugal'
    return 'Wasteful'
