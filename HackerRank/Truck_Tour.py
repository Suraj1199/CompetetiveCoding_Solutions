def truckTour(petrolpumps):
    score=[0]*len(petrolpumps)
    score[0]=petrolpumps[0][0]-petrolpumps[0][1]
    starting_point=0
    for i in range(1,len(petrolpumps)):
        if score[i-1]>=0 :
            score[i]=petrolpumps[i][0]-petrolpumps[i][1]+score[i-1] 
        else:
            score[i]=petrolpumps[i][0]-petrolpumps[i][1]
            starting_point=i

    return starting_point

if __name__ == '__main__':
    n = int(input().strip())
    petrolpumps = []
    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))
    result = truckTour(petrolpumps)
    print(result)
