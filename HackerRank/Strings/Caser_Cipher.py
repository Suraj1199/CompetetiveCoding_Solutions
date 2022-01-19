ef caesarCipher(s, k):
    ans = ''
    for i in s:
        if i.isalpha():
            x = ord('a') if i.islower() else ord('A')
            ans += chr(x + (ord(i) - x + k) % 26)
        else:
            ans += i
    return ans

if __name__ == '__main__':
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
