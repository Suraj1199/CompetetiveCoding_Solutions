n, t = map(int, input().rstrip().split())
widths = list(map(int, input().rstrip().split()))
cases = []
for _ in range(t):
    cases.append(list(map(int, input().rstrip().split())))
for i, j in cases:
    minm = float('inf')
    for k in range(i, j + 1):
        minm = min(minm, widths[k])
    print(minm)
