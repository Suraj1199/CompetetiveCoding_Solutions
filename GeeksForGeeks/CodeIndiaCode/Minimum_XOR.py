for _ in range(int(input())):
    n = int(input())
    nb = list(bin(n)[2:])
    s = len(nb)
    x = (1 << s) - 1
    if n == x:
        print(1 << s)
    else:
        for i in range(s - 1, 0, -1):
            if nb[i] == '0':
                break
        print(1 << (s - i - 1))

