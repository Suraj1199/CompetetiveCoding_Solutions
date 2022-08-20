def matrixRotation(matrix, r):
    n1, n2 = len(matrix), len(matrix[0])
    for i in range(n1):
        for j in range(n2):
            l = min(min(i, j),min(n1-i-1, n2-j-1)) #current layer
            k = r % (2*(n1+n2-(4*l)-2)) #r % max_rotations
            x, y = i, j
            while k:
                if x == l and y != n2-l-1:#topleft->topright
                    inc = min(k, n2-l-y-1)
                    y += inc
                    k -= inc
                elif y == n2-l-1 and x != n1-l-1:#t_right->b_right
                    inc = min(k, n1-l-x-1)
                    x += inc
                    k -= inc
                elif x == n1-l-1 and y != l:#b_right->b_left
                    inc = min(k, y-l)
                    y -= inc
                    k -= inc
                else:#bottom left->top left
                    inc = min(k, x-l)
                    x -= inc
                    k -= inc

            print(matrix[x][y], end=" ")
        print()

if __name__ == '__main__':
    m, n, r = map(int, input().rstrip().split())
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))
    matrixRotation(matrix, r)
