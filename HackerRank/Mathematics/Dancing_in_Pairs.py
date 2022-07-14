import math
def solve(i):
    x = int(math.sqrt(i))
    if x % 2 == 0:
        return "even"
    return "odd"
for _ in range(int(input())):
    result = solve(int(input()))
    print(result)
