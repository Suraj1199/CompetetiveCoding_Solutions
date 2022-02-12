N = int(input())
data = [int(x) for x in input().split()]
ans = "No" if data[-1] % 10 != 0 else "Yes"
print(ans)
