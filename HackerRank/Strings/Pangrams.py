def pangrams(s):
    x = 0
    for i in s.lower():
        if i.isalpha():
            x |= (1 << (ord(i) - ord('a')))
    return 'pangram' if x == 67108863 else 'not pangram'

if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)
