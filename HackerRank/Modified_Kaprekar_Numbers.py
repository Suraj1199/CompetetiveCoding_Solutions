def kaprekarNumbers(p, q):
    # Write your code here
    kaprekar = []
    for i in range(p,q+1):
        b_str = str(i**2)
        
        if(int(b_str)<=9):
            if(int(b_str)==1):
                kaprekar.append(i)
        elif(int(b_str[0:(len(b_str)//2)])+int(b_str[len(b_str)//2:len(b_str)])==i):
            kaprekar.append(i)

    if (len(kaprekar)==0):
        return "INVALID RANGE"
    else:
        return ' '.join(map(str, kaprekar))

if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    print(kaprekarNumbers(p, q))
