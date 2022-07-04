import math
def solve(n, k, s):
    s= [int(x) for x in s]
    rolling_sum=sum(s[:k+1])
    num_pairs=0
    for i in range(k,n+k):
        if s[i-k]:
            num_pairs+=2*rolling_sum-1
            rolling_sum-=1
        if i+1<n:
            rolling_sum+=s[i+1] 
    d=math.gcd(num_pairs, n**2)
    return f'{int(num_pairs/d)}/{int(n**2/d)}' 

if __name__ == '__main__':
    for t_itr in range(int(input().strip())):
        n , k = map(int, input().rstrip().split())
        s = input()
        result = solve(n, k, s)
        print(result)

