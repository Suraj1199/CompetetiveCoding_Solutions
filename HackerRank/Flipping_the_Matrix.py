def flippingMatrix(matrix):
    out = 0
    for i in range(n):
        for j in range(n):
            list = [matrix[i][j],matrix[i][2*n-1-j],matrix[2*n-1-i][j],matrix[2*n-1-i][2*n-1-j]]
            out +=max(list)
    return out

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        matrix = []
        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))
        result = flippingMatrix(matrix)
        print(result)
