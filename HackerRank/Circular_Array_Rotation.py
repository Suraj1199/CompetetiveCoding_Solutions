def circularArrayRotation(a, n, k, queries):
    k %= n
    ra = [-1] * n
    for i in range(n):
        ra[(i + k) % n] = a[i]
    for q in queries:
        print(ra[q])
        
if __name__ == '__main__':
    n, k, q = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))
    queries = []
    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)
    circularArrayRotation(a, n, k, queries)
