from math import gcd

n, q = map(int, input().split())
s = set(map(int, input().split()))
s = list(s)
n = len(s)
for i in range(1, n):
    s[i] -= s[0]

if n > 1:
    g = s[1]
else:
    g = s[0]
for i in range(2, n):
    g = gcd(g, s[i])

while (q != 0):
    p = int(input())
    if n == 1:
        print(s[0]+p)
    else:
        print(gcd(g, s[0]+p))
    q -= 1
