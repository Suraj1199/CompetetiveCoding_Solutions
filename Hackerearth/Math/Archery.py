from math import gcd
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    if n == 1:
        print(a[0])
        continue
    lcm = lambda x, y : (x * y) // gcd(x, y)
    ans = lcm(a[0], a[1])
    for i in range(2, n):
        ans = lcm(ans, a[i])
    print(ans)
