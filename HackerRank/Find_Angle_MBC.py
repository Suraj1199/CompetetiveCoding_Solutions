import math
a = int(input())
b = int(input())
ans = str(round(math.degrees(math.atan(a / b)))) + u'\N{DEGREE SIGN}'
print(ans)
