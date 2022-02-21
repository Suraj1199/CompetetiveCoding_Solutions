for _ in range(int(input())):
    n, k = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    ans = list(range(1, n + 1))
    j = 0
    for i in a:
        ans[i - 1], ans[j] = ans[j], ans[i - 1]
        j = i
    for x in ans:
        print(x, end=" ")
    print()
    
