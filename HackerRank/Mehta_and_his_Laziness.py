from collections import Counter
from math import sqrt
from functools import reduce
from fractions import Fraction

def get_prime_exponents(n):
    '''
        returns the exponents of prime factorization of n 
    '''
    
    prime_factors = []
    # if n is not a prime there should be a prime divisor smaller than sqrt(n)
    for i in range(2, int(sqrt(n)) + 1):
        while n % i == 0:
            prime_factors.append(int(i))
            n = n / i
    
    # if n is prime
    if n > 2:
        prime_factors.append(int(n))
    
    # return the exponents
    return [*Counter(prime_factors).values()]

def solve(n):
    # easy cases: n is not divisible by 4 or equal to 4
    if n%4 or n==4:
        return '0'
    
    exponents=get_prime_exponents(n)
    
    # find if n is an perfect square
    n_is_square= all([not z%2 for z in exponents])
    
    # num of proper divisors is (e1+1)*(e2+1)*...
    q=reduce(lambda x,y: x*y, [z+1 for z in exponents])-1
    
    # reduce exponent of 2 by 2 since we want even perfect square divisors
    exponents[0]-=2
    
    # num of perfect square divisors is (e1+2)//2*(e2+2)//2*...
    p=reduce(lambda x,y: x*y, [(z+2)//2 for z in exponents]) - n_is_square # if n is a perfect square, reduce p by 1
    
    # make p, q coprime
    f= Fraction(p,q)
    p, q = f.numerator, f.denominator
      
    return f'{p}/{q}'

if __name__ == '__main__':
    for t_itr in range(int(input().strip())):
        n = int(input().strip())
        result = solve(n)
        print(result)
