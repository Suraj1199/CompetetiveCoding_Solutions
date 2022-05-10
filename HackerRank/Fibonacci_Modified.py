t1, t2, n = map(int, input().rstrip().split())
for _ in range(n - 2):
    tmp = t1 + t2 ** 2
    t1 = t2
    t2 = tmp
print(t2)

