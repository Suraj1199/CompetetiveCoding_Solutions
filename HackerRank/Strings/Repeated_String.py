from bisect import bisect_left
def repeatedString(s, n):
    idx = []
    for i, c in enumerate(s):
        if c == 'a':
            idx.append(i)
    ans = len(idx) * (n // len(s))
    if idx:
        i = bisect_left(idx, n % len(s))
        ans += i
    return ans

if __name__ == '__main__':
    s = input()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)
