for _ in range(int(input())):
    a, b, c = map(int, input().split(" "))
    x = (a % 2 == 0) + (b % 2 == 0) + (c % 2 == 0)
    print(min(x, 3 - x))
