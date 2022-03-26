for _ in range(int(input())):
    n, k = map(int, input().split())
    a = map(int, input().split())
    for i in a:
        if i <= 0:
            k -= 1
    ans = 'YES' if k > 0 else 'NO'
    print(ans)
