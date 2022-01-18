def lonelyinteger(a):
    x = a[0]
    for i in a[1:]:
        x ^= i
    return x

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = lonelyinteger(a)
    print(result)
