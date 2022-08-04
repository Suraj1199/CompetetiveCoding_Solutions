t = int(input().strip())
for a0 in range(t):
    n,k = map(int, input().split(" "))
    
    if k == 0:
        print (*list(range(1, n+1)))
    elif (n/k) % 2 != 0:
        print ("-1")
    else:
        add = True
        perm = []
        
        for i in range(1, n+1):
            if add:
                perm.append(i+k)
                
            else:
                perm.append(i-k)
                
            if i % k == 0:
                if add:
                    add = False
                else:
                    add = True
        print (*perm)
