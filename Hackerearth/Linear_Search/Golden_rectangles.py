n = int(input())
c = 0
for _ in range(n):
    a, b = map(int, input().split(" "))
    if 1.6 <= a / b <= 1.7 or 1.6 <= b / a <= 1.7:
        c += 1
print(c)
