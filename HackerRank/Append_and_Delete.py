s = input()
t = input()
k = int(input())
n, m = len(s), len(t)
i = 0
while i < min(n, m) and s[i] == t[i]:
    i += 1
if m + n < k or ((m + n) - 2 * i) <= k and ((m + n) - 2 * i) % 2 == k % 2:
    print('Yes')
else:
    print('No')
