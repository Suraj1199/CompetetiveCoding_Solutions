def gemstones(arr):
    arr = list(map(set, arr))
    a1 = arr[0]
    notgem = 0
    for c in a1:
        for ar in arr[1:]:
            if c not in ar:
                notgem += 1
                break
    return len(a1) - notgem
                

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)
    result = gemstones(arr)
    print(result)
