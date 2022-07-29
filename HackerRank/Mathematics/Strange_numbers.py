import os
import heapq as hq
from collections import defaultdict
import bisect as bs

DMAX = 18

work = [(1,i) for i in range(10)]
# strange = defaultdict(set)
strange = set()
hq.heapify(work)

while work:
    d,n = hq.heappop(work)
    if d>DMAX: break
    # strange[d].add(n)
    strange.add(n)
    for k in range(max(2,d),DMAX+1): # exclude d=1 and n=0
        if len(str(n*k)) == k:
            hq.heappush(work,(k,n*k))

strange = sorted(strange)

def solve(a,b):
    return bs.bisect_right(strange,b) - bs.bisect_left(strange,a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = solve(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
