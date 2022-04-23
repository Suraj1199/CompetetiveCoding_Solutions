from collections import defaultdict
def pairs(k, arr):
    h = defaultdict(int)
    c = 0
    for a in arr:
        if a + k in h: 
            c += h[a + k]
        if a - k in h: 
            c += h[a - k]
        h[a] += 1
    return c
if __name__ == '__main__':
    n, k = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    print(result)
