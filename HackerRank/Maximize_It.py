from itertools import product

K, M = map(int, input().split())
numlists = []
for _ in range(K):
    n, l = input().split(' ', 1)
    numlists.append(list(map(int, l.split())))
    
combs = list(product(*numlists))
print(max([sum(map(lambda x:(x**2)%M, c))%M for c in combs]))
