def bomberMan(n, grid):

    if n == 1:
        return grid

    if n % 2 == 0:
        return [r.replace(".", "O") for r in grid]

    thirdGrid = explodeBomb(grid)
    fithGrid = explodeBomb(thirdGrid)
    return fithGrid if ((n - 1) / 2) % 2 == 0 else thirdGrid

def explodeBomb(grid):
    R = len(grid)
    C = len(grid[0])

    neighbours = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
    transformedGrid = [list(r) for r in grid]
    fullGird = [["O"] * C for _ in range(R)]

    bombs = locateBomb(transformedGrid)

    for b in bombs:
        for n in neighbours:
            if 0 <= b[0] + n[0] < R and 0 <= b[1] + n[1] < C:
                fullGird[b[0] + n[0]][b[1] + n[1]] = "."

    return ["".join(r) for r in fullGird]

def locateBomb(grid):
    locations = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                locations.append((i, j))
    return locations

if __name__ == '__main__':
    r, c, n = map(int, input().rstrip().split())
    grid = []
    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)
    result = bomberMan(n, grid)
    print('\n'.join(result))
