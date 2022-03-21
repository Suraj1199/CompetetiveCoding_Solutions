steps = int(input().strip())
path = input()
c = ans = 0
for i in range(steps):
    if path[i] == 'D':
        c -= 1
    else:
        c += 1
        if c == 0:
            ans += 1
print(ans)
