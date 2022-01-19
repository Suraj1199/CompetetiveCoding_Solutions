from collections import Counter

def migratoryBirds(arr):
    h = Counter(arr)
    print(h)
    return sorted(h, key=h.get, reverse=True)[0]

if __name__ == '__main__':
    arr_count = int(input())
    arr = list(map(int, input().rstrip().split(" ")))
    result = migratoryBirds(arr)

    print(result)
