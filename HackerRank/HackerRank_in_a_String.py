w = 'hackerrank'
for _ in range(int(input())):
    s = input()
    i = 0
    for c in s:
        if c == w[i]:
            i += 1
        if i == len(w):
            break
    if i == len(w):
        print('YES')
    else:
        print('NO')
        
