for _ in range(int(input())):
    n = int(input())
    x = n
    ans = 0
    while x > 0:
        r = x % 10
        if r != 0 and n % r == 0:
            ans += 1
        x //= 10
    print(ans)
