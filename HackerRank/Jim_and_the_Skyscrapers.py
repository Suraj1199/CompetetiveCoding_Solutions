def solve(arr):
    arr.append(2**64)
    idx, routes = 0, 0
    stack, m = [], {}
    while idx < len(arr):
        if stack == [] or arr[idx] <= stack[-1]:
            stack.append(arr[idx])
            if arr[idx] in m:
                m[arr[idx]] += 1
            else:
                m[arr[idx]] = 1
            idx += 1
        else:
            top = stack.pop()
            if top in m and top < arr[idx]:
                routes += m[top] * (m[top] - 1) 
                del m[top]
    return(routes)

if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    print(solve(arr))
