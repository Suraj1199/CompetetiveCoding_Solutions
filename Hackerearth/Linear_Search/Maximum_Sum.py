n = int(input())
a = list(map(int, input().split(" ")))
ans = num = 0
for i in range(n):
  if a[i] < 0:
    continue
  ans += a[i]
  num += 1
if num == 0:
  ans = max(a)
  num = 1
print(ans, num)
