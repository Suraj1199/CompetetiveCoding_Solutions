from collections import Counter
def organizingContainers(container,n):
    row_sums = [sum(row) for row in container]
    column_sums =[sum(col) for col in zip(*container)] 
    return "Possible" if Counter(row_sums)==Counter(column_sums) else "Impossible"    

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        container = []
        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))
        print(organizingContainers(container, n))
