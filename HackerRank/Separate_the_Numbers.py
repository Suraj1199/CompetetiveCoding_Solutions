def separateNumbers(s):
    x=''
    for i in range(len(s)//2):
        x=s[:i+1]
        t=x
        while(len(t)<len(s)):
            x=int(x)+1
            t+=str(x)
        if(t==s):
            return "YES "+s[:i+1]
    return "NO" 

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        s = input()
        print(separateNumbers(s))

