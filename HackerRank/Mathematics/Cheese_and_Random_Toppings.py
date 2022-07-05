from math import gcd
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
fac = [1]*51
for i in range(2, 51):
    fac[i] = fac[i-1]*i


class CRT:
    ''' for solving a system of equations : x = a1 (mod n1)
        x = a2 (mod n2) , x = a3 (mod n3) , x = a4 (mod n4) 
        ... . It will give the x mod (LCM(n1,n2,n3,n4,..))
    '''

    def __init__(self, num):
        ''' num = number of equations
            a = list of a's 
            n = list of n's
        '''
        self.num = num
        self.a = [1]*num
        self.n = [1]*num

    def lcm(self, a, b):
        return (a*b//gcd(a, b))

    def GCD(self, a, b):  # solves a*x + b*y == gcd(a,b)
        x = 1
        y = 0
        x1, y1, a1, b1 = 0, 1, a, b
        while(b1):
            q = a1//b1
            x, x1 = x1, x-q*x1
            y, y1 = y1, y-q*y1
            a1, b1 = b1, a1-q*b1
        return(x, y)

    def solve2(self, a1, n1, a2, n2):
        ''' solving two equations x = a1 (mod n1) and x = a2 (mod n2) 
            returns the x (mod LCM(a1,a2))
        '''
        x1 = self.GCD(n1, n2)[0]
        d = gcd(n1, n2)
        if (a1-a2) % d != 0:
            return -1
        ans = -x1*(a1-a2)//d*n1+a1
        mod = self.lcm(n1, n2)
        ans = (ans % mod+mod) % mod
        return ans

    def solve(self):
        ''' solve the system of equations '''
        ans = self.a[0]
        N = self.n[0]
        for i in range(1, self.num):
            ans = self.solve2(ans, N, self.a[i], self.n[i])
            if ans == -1:
                return -1
            N = self.lcm(N, self.n[i])
        return ans


def comb(m, n, p):
    if m < n:
        return 0
    ans = fac[m]//(fac[n]*fac[m-n])
    ans %= p
    return ans


def solve(m, n, M):
    if M == 1:
        return 0
    p = []
    for i in primes:
        if M % i == 0:
            p.append(i)
            while M % i == 0:
                M //= i
    crt = CRT(len(p))
    crt.n = p
    for ind, i in enumerate(p):
        ans = 1
        m_copy = m
        n_copy = n
        while m_copy or n_copy:
            mm = m_copy % i
            nn = n_copy % i
            m_copy //= i
            n_copy //= i
            crt.a[ind] = (crt.a[ind]*comb(mm, nn, i)) % i
    return crt.solve()


for _ in range(int(input())):
    m, n, M = map(int, input().split())
    print(solve(m, n, M))
