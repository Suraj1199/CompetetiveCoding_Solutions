def solve(n, k):
    d  = {}
    d[0] = 1
    for i in range(1, (n+k+1)):
        d[i] = i* d[i-1]
    return( str(d[n+k-1] // (d[k]*d[n-1])%10**9 ))

if __name__ == '__main__':
    for t_itr in range(int(input().strip())):
        n = int(input().strip())
        k = int(input().strip())
        result = solve(n, k)
        print(result)
