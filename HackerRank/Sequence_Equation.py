def permutationEquation(p):
    dic = {p[i]:i+1 for i in range(len(p))}
    return [dic[dic[i+1]]  for i in range(len(p))]

if __name__ == '__main__':
    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    result = permutationEquation(p)
    print('\n'.join(map(str, result)))
