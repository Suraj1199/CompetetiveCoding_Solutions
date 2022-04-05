def maximizingXor(l, r):
    ans = 0
    for a in range(l, r + 1):
        for b in range(a, r + 1):
            ans = max(ans, a ^ b)
    return ans
        
if __name__ == '__main__':
    l = int(input().strip())
    r = int(input().strip())
    result = maximizingXor(l, r)
    print(result)
 
