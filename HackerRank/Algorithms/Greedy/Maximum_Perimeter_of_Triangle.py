def maximumPerimeterTriangle(sticks):
    sticks.sort()
    for i in range(len(sticks) - 1, 1, -1):
        if sticks[i - 2] + sticks[i - 1] > sticks[i]:
            return [sticks[i - 2], sticks[i - 1], sticks[i]]
    return [-1]

if __name__ == '__main__':
    n = int(input().strip())
    sticks = list(map(int, input().rstrip().split()))
    result = maximumPerimeterTriangle(sticks)
    print(result)
