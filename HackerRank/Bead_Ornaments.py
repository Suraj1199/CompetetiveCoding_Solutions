from operator import mul
from functools import reduce

def beadOrnaments(b):
    return int((reduce(mul, map(lambda x: x ** (x - 1), b), 1) * (sum(b) ** (len(b) - 2))) % (7 + 10 ** 9))

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        b_count = int(input().strip())
        b = list(map(int, input().rstrip().split()))
        print(beadOrnaments(b))
