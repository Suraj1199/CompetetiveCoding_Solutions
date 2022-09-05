from itertools import combinations
n=int(input())
l=list(map(int,input().split(" ")))
o=[0]*len(l)
def find_gcd(x,y):
    while (y):
        x,y=y,x % y
    return x
for (i,j) in combinations(range(1,len(l)+1),2):
    if i <= j:
        s=l[i-1:j]
        if len(s)==1:gcd=abs(s[0])   
        else :
            gcd=find_gcd(abs(s[0]),abs(s[1]))        
            for k in range(2,len(s)):
                gcd = find_gcd(gcd,abs(s[k])) 
        summt=(sum(s)-max(s))
        o.append(gcd*summt)
print(max(o)) 
