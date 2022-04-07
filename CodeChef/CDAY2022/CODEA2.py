from collections import Counter
n = int(input())
s = Counter(input())
w = max(s, key=s.get)
if w == 'A':
    print('Alice')
else:
    print('Bob')
