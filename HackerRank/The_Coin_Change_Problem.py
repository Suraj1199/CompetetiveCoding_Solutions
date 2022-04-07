def getWays(n, m, c):
    dp = [1] + [0] * n
    for i in range(m):
        for j in range(c[i], n + 1):
            dp[j] += dp[j - c[i]]
    return dp[n]
if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    c = list(map(int, input().rstrip().split()))
    ways = getWays(n, m, c)
    print(ways)
