dp = [0] * 61
dp[0] = 1
for i in range(1, 61):
    if i % 2:
        dp[i] = dp[i - 1] * 2
    else:
        dp[i] = dp[i - 1] + 1
for _ in range(int(input())):
    print(dp[int(input())])
