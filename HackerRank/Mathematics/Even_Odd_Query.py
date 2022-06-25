def solve(arr, queries):
    result= []
    for i, j in queries:
        if(i<len(arr) and arr[i]==0 and i!=j):
            result.append('Odd')
        else:
            if(arr[i-1]%2==0):
                result.append('Even')
            else:
                result.append('Odd')
    return result

if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    result = solve(arr, queries)
    print('\n'.join(result))
