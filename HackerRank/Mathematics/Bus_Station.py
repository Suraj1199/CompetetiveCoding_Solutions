def solve(A):
    L = sum(A)
    R = 0
    R = 0
    ret = ""
    for i in A[::-1]:
        if L == 0:
            break
        if R % L == 0:
            b = 0
            for j in A:
                b += j
                if b == L:
                    b = 0
                elif b > L:
                    break
            if b == 0:
                ret = str(L)+ " " + ret
        L -= i
        R += i
    return ret

if __name__ == '__main__':
    a_count = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = solve(a)
    print(''.join(map(str, result)))
