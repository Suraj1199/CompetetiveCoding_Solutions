def camelcase(s):
    ans = 1
    for i in s:
        if i.isupper():
            ans += 1
    return ans

if __name__ == '__main__':
    s = input()
    result = camelcase(s)
    print(result)
