import math
def closestNumber(a, b, x):
    f=(math.floor((a**b)/x)*x)
    c=(math.ceil((a**b)/x)*x)
    if((a**b)-f<c-(a**b)):
        return f
    return c

if __name__ == '__main__':
    for t_itr in range(int(input().strip())):
        a, b, x = map(int, input().rstrip().split())
        result = closestNumber(a, b, x)
        print(result)
