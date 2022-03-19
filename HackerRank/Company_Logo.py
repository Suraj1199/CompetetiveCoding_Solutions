from collections import Counter
s = input()
c = Counter(s)
for i in sorted(c, key=lambda x: (-c[x], x))[:3]:
    print(i, c[i])
    
