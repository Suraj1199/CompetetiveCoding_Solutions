def breakingRecords(scores):
    minm, maxm = scores[0], scores[0]
    mmc, mxc = 0, 0
    for s in scores[1:]:
        if s < minm:
            minm = s
            mmc += 1
        elif s > maxm:
            maxm = s
            mxc += 1
    return [mxc, mmc]

if __name__ == '__main__':
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(result)
