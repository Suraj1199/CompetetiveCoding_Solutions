import math
t = int(input())
for _ in range(t):
    x, m = map(int, input().split(" "))
    h = math.ceil(math.log(x,2))
    print(max(m - h, 0))
        
        
