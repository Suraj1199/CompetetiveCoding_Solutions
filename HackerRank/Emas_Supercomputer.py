def twoPluses(grid):
    for i in range(len(grid)):
        grid[i] = list(grid[i])
        grid[i].append('o')
        grid[i].insert(0,'o')
    grid.append(['o' for i in range(len(grid[0]))])
    grid.insert(0,['o' for i in range(len(grid[0]))])
    res = []
    for i in range(1,len(grid)-1):
        for j in range(1, len(grid[0])-1):
            if grid[i][j]=='G':
                currCord = []
                currCord.append((i,j))
                area = 1
                start = 1
                res.append([area,currCord.copy()])
                while ((grid[i-start][j]=='G') & (grid[i+start][j]=='G') & (grid[i][j-start]=='G') & (grid[i][j+start]=='G')):
                    currCord.append((i-start,j))
                    currCord.append((i+start,j))
                    currCord.append((i,j-start))
                    currCord.append((i,j+start))
                    area+=4
                    start+=1
                    res.append([area,currCord.copy()])
    result = 0      
    for i in range(len(res)-1):
        for j in range(i+1,len(res)):
            if (len(set(res[i][1]).intersection(set(res[j][1])))==0) & (res[i][0]*res[j][0]>result):
                result = res[i][0]*res[j][0]
    return result

if __name__ == '__main__':
    n,m  = map(int, input().rstrip().split())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = twoPluses(grid)
    print(result)
