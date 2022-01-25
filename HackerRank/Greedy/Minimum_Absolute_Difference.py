def minimumAbsoluteDifference(arr):
    arr.sort()
    minm = float('inf')
    for i in range(len(arr) - 1):
        minm = min(minm, abs(arr[i] - arr[i + 1]))
    return minm

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(result)
