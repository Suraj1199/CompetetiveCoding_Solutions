import collections
def equalizeArray(arr):
    return len(arr)-max(collections.Counter(arr).values())

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = equalizeArray(arr)
    print(result)
