for _ in range(int(input())):
    m, n = int(input().strip()), int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    h = {}
    for i, a in enumerate(arr):
        if m - a in h:
            break
        h[a] = i + 1
    print(h[m - a], i + 1)
