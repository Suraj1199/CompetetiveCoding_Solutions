import math
from collections import defaultdict
def factors(n):
    
    res=defaultdict(int)
    while n&1!=1:
        res[2]+=1
        n//=2
    for i in range(3,int(pow(n,0.5))+1,2):
        while n%i==0:
            res[i]+=1
            n//=i
    if n>2:
        res[n]+=1
    return res


if __name__ == '__main__':
    n, k = map(int, input().split())
    A = list(map(int, input().rstrip().split()))
    hcf=A[0]
    for i in range(1,n):
        hcf=math.gcd(hcf,A[i])
    factor=factors(hcf).keys()
    M=0
    for x in factor:
        M=max(M,k-k%x)
    print(M)
