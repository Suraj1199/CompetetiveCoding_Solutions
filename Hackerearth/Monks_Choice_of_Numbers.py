for _ in range(int(input())):
  n, k = map(int, input().split(" "))
  a = list(map(int, input().split(" ")))
  ans = []
  for i in range(n):
    ans.append(bin(a[i])[2:].count('1'))
  print(sum(sorted(ans, reverse=True)[:k]))
