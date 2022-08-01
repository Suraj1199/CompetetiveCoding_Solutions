def surfaceArea(a):
    s = 0
    for k in range(len(a)):
        for i in range(len(a[k])):
            back = min(a[k][i], a[k][i-1]) if i > 0 else 0
            side = min(a[k][i], a[k-1][i]) if k > 0 else 0
            s += 2 + a[k][i]*4 - back*2 - side*2
    return s

if __name__ == '__main__':
    H, W = map(int, input().rstrip().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))
    result = surfaceArea(A)
    print(result)
