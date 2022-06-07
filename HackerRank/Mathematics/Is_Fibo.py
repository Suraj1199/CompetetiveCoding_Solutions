s, a, b = set(), 0, 1
while a <= 1e10:
    s.add(a)
    a, b = b, a + b
for _ in range(int(input().strip())):
    n = int(input().strip())
    if n in s:
        print('IsFibo')
    else:
        print('IsNotFibo')

    
