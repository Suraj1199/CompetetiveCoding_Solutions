from collections import Counter

for i in range(int(input())):
   s=input()
   ans=1
   c=Counter(s).values()
   for i in c:
       ans*=i
   print(ans%(10**9+7))
