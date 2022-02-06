def average(array):
    a = set(array)
    return sum(a) / len(a)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
