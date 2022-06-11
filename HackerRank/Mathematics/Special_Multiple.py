for _ in range(int(input())):
    i = 1
    c = int(input())
    while True:
        j = int(bin(i)[2:].replace('1','9'))
        if j % c == 0:
            break
        i+=1
    print(j)
