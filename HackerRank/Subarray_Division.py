def birthday(s, d, m):
    x = sum(s[:m])
    ans = int(x == d)
    for i in range(len(s) - m):
        x = x - s[i] + s[i + m]
        ans += int(x == d)
    return ans

if __name__ == '__main__':
     n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    first_multiple_input = input().rstrip().split()
    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    result = birthday(s, d, m)
    print(result)
