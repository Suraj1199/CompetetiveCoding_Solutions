from collections import Counter
m = int(input())
h = Counter(map(int, input().split(" ")))
n = int(input())
ans = 0
for _ in range(n):
    i, j = map(int, input().split(" "))
    if i in h and h[i] != 0:
        ans += j
        h[i] -= 1
print(ans)
