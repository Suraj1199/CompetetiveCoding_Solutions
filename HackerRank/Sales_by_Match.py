from collections import Counter
def sockMerchant(n, ar):
    h = Counter(ar)
    ans = 0
    for i in h:
        ans += h[i] // 2
    return ans

if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
