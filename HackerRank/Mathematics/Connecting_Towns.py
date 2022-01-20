def connectingTowns(n, routes):
    ans = 1
    for i in routes:
        ans *= i
    return ans % 1234567

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)
	print(result)
