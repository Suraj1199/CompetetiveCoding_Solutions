for _ in range(int(input())):
    x, y, z = map(int, input().split())
    a = abs(x - z)
    b = abs(y - z)
    if a < b:
        print('Cat A')
    elif a > b:
        print('Cat B')
    else:
        print('Mouse C')
