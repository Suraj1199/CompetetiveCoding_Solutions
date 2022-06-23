import math
def solve(x):
    C = (math.sqrt(3)*math.sqrt(3888*x*x-1)+x*108)**(1./3.)
    return math.floor((C/9**(1./3.)+1/(3**(1./3.)*C)-1)/2+0.0000001)

if __name__ == '__main__':
    for t_itr in range(int(input().strip())):
        x = int(input().strip())
        result = solve(x)
        print(result)
