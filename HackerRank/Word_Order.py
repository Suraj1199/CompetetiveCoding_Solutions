from collections import OrderedDict
h = OrderedDict()
for _ in range(int(input())):
    s = input()
    h[s] = h.get(s, 0) + 1
print(len(h))
print(' '.join(map(str, h.values())))
