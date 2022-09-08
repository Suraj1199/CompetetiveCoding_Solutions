def runningTime(arr):
    n = len(arr)
    result = 0
    for i in range(1,n):
        target = arr[i]
        j = i - 1
        while (j >= 0) and (arr[j] > target):
            arr[j + 1] = arr[j]
            result += 1
            j -= 1
        arr[j + 1] = target 
    return result

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = runningTime(arr)
    print(result)
