from collections import Counter
n = int(input())
c = Counter(input().split(" "))
print(min(c, key=c.get))
