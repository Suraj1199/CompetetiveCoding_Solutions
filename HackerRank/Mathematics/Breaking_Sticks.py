import math
def divisor(number):
    for i in range(2,math.ceil(math.sqrt(number))+1):
        if (number % i == 0):

            return number//i
        
    return 1

def largest(n):
    if n == 1:
        return 1
    s = n
    a = n
    while a > 1:
        d = divisor(a)
        s+=d
        a = d
    return s

t = int(input())
a = list(map(int,input().split()))
ans = 0
for x in a:
    ans+= largest(x)
print(ans)
ans = 0
for x in a:
    ans+= largest(x)
print(ans)
