def fact(n):
    if n < 2:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    n = int(input().strip())
    print(fact(n))
