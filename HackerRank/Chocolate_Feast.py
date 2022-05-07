def chocolateFeast(n, c, m):
    choco, eat, wp = n // c, 0, 0
    while choco > 0:
        eat += choco
        wp += choco
        choco = wp // m
        wp = wp % m
    return eat;

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, c, m = map(int, input().rstrip().split())
        result = chocolateFeast(n, c, m)
        print(result)
