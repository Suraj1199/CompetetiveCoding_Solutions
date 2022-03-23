for _ in range(int(input())):
    n = int(input())
    b = len(bin(n)[2:])
    s = 0
    for i in range(b):
        s += (1 << i) - 1
    x = (1 << b) - 1
    print(s - (x - n))
    
