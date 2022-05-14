n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
arr.sort()
if n % 2 == 0:
    print((arr[n // 2] + arr[n // 2 + 1]) / 2)
else:
    print(arr[n // 2])
