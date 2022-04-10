for _ in range(int(input())):
    s = list(input())
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    if i < 0:
        print('no answer')
        continue
    j = len(s) - 1
    while j > i and s[j] <= s[i]:
        j -= 1
    s[i], s[j] = s[j], s[i]
    s[i+1:] = s[i+1:][::-1]
    print(''.join(s))
