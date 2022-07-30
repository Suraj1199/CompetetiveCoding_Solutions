import math
import sys

n = int(sys.stdin.readline())
numbers = map(int, sys.stdin.readline().split())
witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
Primes = []
IsPrime = [True] * 100001
for p in range(2, 100000):
    if not(IsPrime[p]) : continue 
    Primes.append(p)
    mult = p * p
    while mult < 100001:
        IsPrime[mult] = False
        mult += p
        
def GetRidOf2(n):
    while n % 2 == 0:
        n //= 2
    return n

def IsComposite(n, a, s, d):
    if pow(a, d, n) == 1: return False
    for r in range(s) :
        if pow(a, (1 << r) * d, n) == n - 1: return False   
    return True

def IsPrime(n):
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1   
    for a in witnesses:
        if IsComposite(n, a, s, d) : return False   
    return True
   
def IsNPowerOfPrime(n):
    if IsPrime(n): return True
    sqrt = int(math.sqrt(n))
    if sqrt * sqrt == n and IsPrime(n):
        return True      
    return False

def IsNSquare(n):
    sqrt = int(math.sqrt(n))
    return (sqrt * sqrt == n)
    
def Factor(n):
    nbFactors = 0
    sumFactors = 0
    if n % 2 == 0:
        nbFactors += 1
        n = GetRidOf2(n)       
    if IsNSquare(n) : 
        sumFactors = 1
        n = int(math.sqrt(n))   
    for prime in Primes :
        if n == 1 : break   
        if n % prime != 0 : continue    
        nbFactors += 1
        n //= prime
        while n % prime == 0:
            n //= prime           
    if n == 1:
        return (nbFactors, sumFactors)       
    if IsNPowerOfPrime(n):
        return (nbFactors + 1, sumFactors)      
    return (nbFactors + 2, sumFactors)
    
result = [[0, 0], [0, 0]]
for n in numbers:
    (nb, s) = Factor(n)
    result[nb % 2][s] += 1   
finalResult = result[0][0] + result[0][1]
finalResult = max(finalResult, result[0][0] + result[1][0])
finalResult = max(finalResult, result[1][1] + result[1][0])
finalResult = max(finalResult, result[1][1] + result[0][1])
print(finalResult)
