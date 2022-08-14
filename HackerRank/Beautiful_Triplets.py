def beautifulTriplets(d, c):
    gc = 0
    for i in range(n):
        if c[i]+d in c and c[i]+2*d in c:
            gc+=1
    return gc

if __name__ == '__main__':
    n, d = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))
    result = beautifulTriplets(d, arr)
    print(result)
