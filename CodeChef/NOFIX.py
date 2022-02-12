t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    k = 0
    for i in range(n):
        if i + k == a[i] - 1:
            k += 1
    print(k)
