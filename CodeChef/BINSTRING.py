for _ in range(int(input())):
    n = int(input())
    s = input() + '.'
    a = ''
    for i in range(n):
        if s[i] != s[i + 1]:
            a += s[i]
    print(len(a))
        
