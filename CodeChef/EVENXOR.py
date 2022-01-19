t = int(input())
bad = lambda x: bin(x)[2:].count('1') % 2 != 0
for _ in range(t):
    n = int(input())
    i = 0
    num = 3
    for i in range(n):
        while bad(num):
            num += 1
        print(num, end=" ")
        num += 1
    print()
