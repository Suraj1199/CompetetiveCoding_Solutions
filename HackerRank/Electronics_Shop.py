def getMoneySpent(keyboards, drives, b):
    ans = -1
    for d in drives:
        for k in keyboards:
            if k + d <= b:
                ans = max(ans, k + d)
    return ans            

if __name__ == '__main__':
    b, n, m = map(int, input().split())
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)
