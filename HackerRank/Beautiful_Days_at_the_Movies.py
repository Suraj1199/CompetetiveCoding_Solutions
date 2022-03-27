i, j, k = map(int, input().split())
ans = 0
for s in range(i, j + 1):
    ans += (abs(s - int(str(s)[::-1])) % k == 0)
print(ans)
