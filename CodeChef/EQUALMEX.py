def mex(a):
    m = 0
    for i in set(a):
        if m != i:
            break
        m += 1
    return m    
    
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    a.sort(reverse=True)
    a1, a2 = [], []
    for i in range(2 * n):
        if i % 2 == 0:
            a1.append(a[i])
        else:
            a2.append(a[i])
    if mex(a1) == mex(a2):
        print("YES")
    else:
        print("NO")
    
