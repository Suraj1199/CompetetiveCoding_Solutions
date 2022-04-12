l = int(input().strip())
a = input()
s = list(set(a))
def length(t):
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            return 0
    return len(t)
ans = 0
for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        t = [c for c in a if c in [s[i], s[j]]]
        ans = max(ans, length(t))
print(ans)
