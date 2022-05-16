def pokerNim(k, c):
    res=0
    for i in c:
        res^=i
    if(res):
        return("First")
    else:
        return("Second")

for _ in range(int(input().strip())):
    n, k = input().rstrip().split()
    c = list(map(int, input().rstrip().split()))
    result = pokerNim(k, c)
    print(result)
