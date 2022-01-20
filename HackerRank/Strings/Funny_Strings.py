def funnyString(s):    
    def solve(s):
        diff = []
        prev = s[0]
        for c in s[1:]:
            diff.append(abs(ord(prev) - ord(c)))
            prev = c
        return diff
    return "Funny" if solve(s) == solve(s[::-1]) else "Not Funny"
 
if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = funnyString(s)
	print(result)
