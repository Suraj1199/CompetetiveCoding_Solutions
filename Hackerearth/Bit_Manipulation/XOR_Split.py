for _ in range(int(input())):
    n = int(input())
    x = bin(n)[2:]
    if x.count('1') > 1:
        print(1)
    else:
        print(0)
