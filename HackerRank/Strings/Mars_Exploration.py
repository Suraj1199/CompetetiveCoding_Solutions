s = input()
n = len(s)
ans = 0
e = 'SOS' * (n // 3)
for i in range(n):
    ans += (s[i] != e[i])
print(ans)
