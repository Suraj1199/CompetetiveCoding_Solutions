n = int(input())
divisors = [[1] for i in range(n)]
for i in range(2,n):
    for j in range(i, n, i):
        divisors[j].append(i)
    divisors[i].reverse()
tups = 0
for i in range(1, n):
    divs = set()
    for j in range(i, n, i):
        divisors[j].pop()
    for j in range(i, n, i):
        divs.update(divisors[n-j])
    tups += len(divs)
print(tups)
