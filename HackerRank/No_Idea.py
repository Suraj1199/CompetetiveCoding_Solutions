n, m = map(int, input().split())
a = list(map(int, input().split()))
ha = set(map(int, input().split()))
sa = set(map(int, input().split()))
ans = 0
for i in range(n):
    if a[i] in ha:
        ans += 1
    elif a[i] in sa:
        ans -= 1
print(ans)
