def maximumSum(a, m):
    prefix = [None] * len(a)
    prefix[0] = a[0] % m
    for i in range(1, len(a)):
        prefix[i] = (prefix[i-1] + a[i]) % m
    best = max(prefix)
    numbered = enumerate(prefix)
    sort = sorted(numbered, key=lambda x: x[1])
    best = best - m
    for i in range(1, len(sort)):
        candidate_value = sort[i-1][1] - sort[i][1]
        if candidate_value < 0 and candidate_value > best:
            if sort[i-1][0] > sort[i][0]:
                best = candidate_value
    return(best + m)
    
if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, m = map(int, input().rstrip().split())
        a = list(map(int, input().rstrip().split()))
        print(maximumSum(a, m))
