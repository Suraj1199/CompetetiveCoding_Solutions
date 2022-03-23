from collections import Counter
for _ in range(int(input())):
    n = int(input())
    h = Counter(input())
    print(2 * min(h['0'], h['1']) + (h['0'] != h['1']))
