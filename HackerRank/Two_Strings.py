from collections import Counter
def twoStrings(s1, s2):
    c1 = Counter(s1) 
    c2 = Counter(s2)
    for c in c1:
        if c in c2:
            return "YES"
    return "NO"

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        print(result)
