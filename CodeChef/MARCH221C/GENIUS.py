for _ in range(int(input())):
    n, x = map(int, input().split(" "))
    if x == 0:
        print('YES\n0 0', n)
        continue
    a = x // 3 + (x % 3 != 0)
    b = (3 - x % 3) % 3
    c = n - (a + b)
    if c < 0:
        print("NO")
    else:
        print("YES")
        print(a, b, c)
    
