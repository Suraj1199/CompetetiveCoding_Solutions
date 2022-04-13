def squares(a, b):
    numOfSquares, x = 0, 1
    while x*x < a:
        x += 1
    while x*x <= b:
        numOfSquares += 1
        x += 1    
    return numOfSquares;

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        a, b = map(int, input().rstrip().split())
        result = squares(a, b)
        print(result)
