def solve(s):
    s = s.split(" ")
    for i, w in enumerate(s):
        if len(w) > 0:
            s[i] = w[0].upper() + w[1:]
    return ' '.join(s)
        
if __name__ == '__main__':
    s = input()

    result = solve(s)
    print(result)
