def getMinimumCost(k, c):
    c.sort(reverse = True)
    cost = 0
    for i in range(0, len(c), k):
        cost += sum(c[i:i+k]) * (i//k + 1)
    return cost

if __name__ == '__main__':
    n, k = map(int, input().split())
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    print(minimumCost)
