from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    h = Counter(s)
    if n <= 2 or len(h) == 1:
        print("YES")
        continue
    if n % 2 == 0:
        if h['0'] == h['1'] or (h['0'] % 2 == 0 and h['1'] % 2 == 0):
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
