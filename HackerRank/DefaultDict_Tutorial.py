from collections import defaultdict
n, m = map(int, input().split(" "))
d = defaultdict(list)
for i in range(1, n + 1):
    d[input()].append(str(i))
for _ in range(m):
    x = input()
    if x not in d:
        print(-1)
    else:
        print(' '.join(d[x]))
    
