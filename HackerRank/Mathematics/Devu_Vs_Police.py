lim = 3200
mark = bytearray(lim)
primes = [2]
for i in range(3, lim, 2):
    if mark[i]: continue
    primes.append(i)
    for j in range(3 * i, lim, 2 * i):
        mark[j] = 1

def factor(n):
    f = {}
    for p in primes:
        if p * p > n: break
        while n % p == 0:
            n //= p
            f[p] = f.get(p, 0) + 1
    if n > 1: f[n] = 1
    return f

T = int(input())
for t in range(T):
    n1, k1, n2, k2, n = map(int, input().split())
    if n1 == 0:
        f1 = 1 if k1 == 0 else 0
    else:
        f1 = pow(n1, k1, n) or n
    if n2 == 0:
        f2 = 1 if k2 == 0 else 0
    else:
        phi = 1
        for p, e in factor(n).items():
            phi *= (p - 1) * p ** (e - 1)
        f2 = pow(n2, k2, phi) or phi
    print(pow(f1, f2, n))
