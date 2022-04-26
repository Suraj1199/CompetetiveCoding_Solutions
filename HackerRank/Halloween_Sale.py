def howManyGames(p, d, m, s):
    count = 0
    while s >= p:
        count += 1
        s -= p
        p = max(p-d, m)
    return count

if __name__ == '__main__':
    p, d, m, s = map(int, input().rstrip().split())
    ans = howManyGames(p, d, m, s)
    print(ans)
