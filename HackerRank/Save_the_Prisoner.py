for _ in range(int(input())):
    n, m, s = map(int, input().split())
    r = (m % n if m % n else n) + s - 1
    a = r % n if r % n else n
    print(a)
