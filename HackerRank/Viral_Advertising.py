n = int(input().strip())
total = 2;
liked = 2;
for _ in range(n-1):
    liked = liked * 3//2
    total += liked
print(total)
