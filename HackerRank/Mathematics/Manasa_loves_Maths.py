def solve(n):
    if int(n) < 100:
        if int(n)%8 == 0 or int(n[::-1])%8 == 0:
            return "YES"
        return "NO"
            
    else:
        multiples_of_8 = []
        for i in range (0, 1000, 8):
            multiples_of_8.append(str(i).zfill(3))
            
        for e in multiples_of_8:
            if e[0] in n:
                m = n.replace(e[0], '', 1)
                if e[1] in m:
                    m = m.replace(e[1], '', 1)
                    if e[2] in m:
                        return "YES"
        return "NO"

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = input()
        result = solve(n)
        print(result)
