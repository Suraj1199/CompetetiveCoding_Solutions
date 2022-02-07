t = int(input())
for _ in range(t):
    n, k = map(int, input().split(" "))
    s = input()
    c = 0
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            c += 1
    if k < c:
        print("NO")
    else:
        k -= c
        if n % 2 != 0:
            print("YES")
        else:
            if k % 2 == 0:
                print("YES")
            else:
                print("NO")