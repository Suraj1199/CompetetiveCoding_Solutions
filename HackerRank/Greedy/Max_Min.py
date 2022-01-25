def maxMin(k, arr):
    arr.sort()
    minm = float('inf')
    for i in range(n - k):
        minm = min(minm, arr[i+k-1] - arr[i])
    return minm
        

if __name__ == '__main__':
    n = int(input().strip())
    k = int(input().strip())
    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)


