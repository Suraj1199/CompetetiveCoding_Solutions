for _ in range(int(input())):
    s = input()
    t = input()
    ans = ''
    for i in range(5):
        if s[i] == t[i]:
            ans += 'G'
        else:
            ans += 'B'
    print(ans)
