from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    h = Counter(map(lambda x: len(bin(x)[2:]), a))
    ans = 0
    for i in h:
        if h[i] > 1:
            ans += h[i] * (h[i] - 1) // 2
    print(ans)
