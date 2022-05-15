for _ in range(int(input())):
    s = input()
    print(sum([abs(ord(s[i])-ord(s[-i-1])) for i in range(len(s)//2)]))

