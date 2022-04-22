def balancedSums(arr):
    n = len(arr)
    lsum, rsum = [0] * (n + 1), [0] * (n + 1)
    for i in range(n):
        lsum[i + 1] = arr[i] + lsum[i]
        rsum[n - i - 1] = arr[n - i - 1] + rsum[n - i]
    for i in range(n):
        if lsum[i] == rsum[i + 1]:
            return 'YES'
    return 'NO'
        
for _ in range(int(input().strip())):
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = balancedSums(arr)
    print(result)
