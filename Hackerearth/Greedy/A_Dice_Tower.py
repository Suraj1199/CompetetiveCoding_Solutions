for _ in range(int(input())):
    n = int(input())
    a = 0
    if n > 40:
        a = n // 14 - 2
        n -= 14 * a
    if n == 21:
        print(1)
    elif 30 <= n <= 40:
        print(2 + a)
    else:
        print(-1)
