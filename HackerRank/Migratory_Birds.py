from collections import Counter
n = int(input())
c = Counter(input().split())
print(max(c, key=lambda x: (c[x], -int(x))))
