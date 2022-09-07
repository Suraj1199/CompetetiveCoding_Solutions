from bisect import bisect_left, bisect_right, insort

def solve(shots, players):
    slower, shigher = [], []
    for s in shots:
        insort(slower, s[0])
        insort(shigher, s[1])
    result = 0
    for p in players:
        start = min(bisect_left(slower,p[0]),bisect_left(shigher,p[0]))
        end = max(bisect_right(shigher,p[1]),bisect_right(slower,p[1]))
        result += end-start
    return result

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    shots = []

    for _ in range(n):
        shots.append(list(map(int, input().rstrip().split())))

    players = []

    for _ in range(m):
        players.append(list(map(int, input().rstrip().split())))

    result = solve(shots, players)
    print(result)

