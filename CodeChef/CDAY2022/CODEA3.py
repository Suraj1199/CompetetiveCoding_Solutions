t = int(input())
c = 0
for _ in range(t):
    x, y = map(int, input().split())
    if x >= 3 and y >= 3 and x + y >= 15:
        c += 1
if c * 2 >= t:
    print('Genius')
else:
    print('Not Genius Yet')
