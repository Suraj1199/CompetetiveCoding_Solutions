s = input() + '.'
c = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        c += 1
    else:
        print('(' + str(c) + ', ' + s[i] + ')', end=' ')
        c = 1
