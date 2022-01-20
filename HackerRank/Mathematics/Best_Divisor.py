from math import ceil, sqrt
def digits(n):
    c = 0
    while n > 0:
        c += n % 10
        n //= 10
    return c
if __name__ == '__main__':
    n = int(input().strip())
    f = [1, n]
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            f.append(i)
            f.append(n // i)
    f = sorted(f, key=digits)
    print(f[-1])
