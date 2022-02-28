for _ in range(int(input())):
    n, k = map(int, input().split(" "))
    ans = 1
    for i in range(k - n + 1, k + 1):
        ans = (ans * i) % 1000000007
    print(ans )

