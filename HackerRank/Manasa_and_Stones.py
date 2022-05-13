for _ in range(int(input().strip())):
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    print(' '.join(map(str,sorted({x*a+(n-1-x)*b for x in range(n)}))))    

