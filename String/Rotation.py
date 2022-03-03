n = int(input())
s = input()
t = input()

for i in range(n):
    if t == s:
        break
    s = s[1:]
    t = t[:-1]
print(i)

