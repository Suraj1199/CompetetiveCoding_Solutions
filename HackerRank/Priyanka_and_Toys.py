def toys(w):
    cnt = 0 
    x = -1
    w.sort()
    for i in w:
        if i > x:
            x = i + 4   
            cnt += 1
    return cnt

if __name__ == '__main__':
    n = int(input().strip())
    w = list(map(int, input().rstrip().split()))
    result = toys(w)
    print(result)
