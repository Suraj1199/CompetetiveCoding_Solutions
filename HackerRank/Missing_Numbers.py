from collections import Counter
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
m = int(input().strip())
brr = list(map(int, input().rstrip().split()))
ca, ba = map(Counter, [arr, brr])
ans = []
for i in ba:
    if i not in ca or (i in ba and ba[i] > ca[i]):
        ans.append(i)
ans.sort()
print(' '.join(map(str, ans)))
