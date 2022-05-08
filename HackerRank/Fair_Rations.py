def fairRations(B):
    count=0
    for a in range(len(B)):
        try:
            if B[a]%2 == 1:
                count+=2
                B[a+1]+=1
        except:
            return 'NO'
    return count

if __name__ == '__main__':
    N = int(input().strip())
    B = list(map(int, input().rstrip().split()))
    result = fairRations(B)
    print(result)
