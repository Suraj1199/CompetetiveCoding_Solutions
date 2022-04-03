from collections import defaultdict
def minimumDistances(a):
    h = defaultdict(list)
    for i in range(len(a)):
        h[a[i]].append(i)
    ans = float('inf')
    for i in h:
        if len(h[i]) > 1:
            p = h[i][0]
            for j in h[i][1:]:
                ans = min(ans, j - p)
                p = j
    return ans if ans != float('inf') else -1
                
if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = minimumDistances(a)
    print(result)     
