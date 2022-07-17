n,m = map(int,input().strip().split(' '))
import itertools
import random  
  

def power(x, y, p): 
      
    res = 1;  
    x = x % p;  
    while (y > 0): 
          
       
        if (y & 1): 
            res = (res * x) % p;   
        y = y>>1; 
        x = (x * x) % p; 
      
    return res; 
  

def miillerTest(d, n): 
      
    # Pick a random number in [2..n-2] 
    # Corner cases make sure that n > 4 
    a = 2 + random.randint(1, n - 4); 
  
    # Compute a^d % n 
    x = power(a, d, n); 
  
    if (x == 1 or x == n - 1): 
        return True; 
  
    while (d != n - 1): 
        x = (x * x) % n; 
        d *= 2; 
  
        if (x == 1): 
            return False; 
        if (x == n - 1): 
            return True; 
  
    # Return composite 
    return False; 
  

def isPrime( n, k): 
      
    if (n <= 1 or n == 4): 
        return False; 
    if (n <= 3): 
        return True; 
    d = n - 1; 
    while (d % 2 == 0): 
        d //= 2; 
  
    for i in range(k): 
        if (miillerTest(d, n) == False): 
            return False; 
  
    return True; 
x = [ '2', '3', '5','7' ]
P=[]
k = 4
b = ""
if len(str(n)) >9:
    i=0
    while i<len(str(n)) and str(n)[i] == str(m)[i]  :
        b+=str(n)[i]
        i+=1 
c = len(b)

for i in range(len(str(n)),len(str(m))+1):
    L = [p for p in itertools.product(x, repeat=i-c)]
   
    for j in range(len(L)):
        a = int(b+''.join(L[j]))
    
        if a>m: 
            break
        if a>n  and isPrime(a,k):
            P.append(a)
        
print(len(P))
