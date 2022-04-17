def alternatingCharacters(s):
    st = []
    c = 0
    for i in s:
        if st and st[-1] == i:
            c += 1
        else:
            st.append(i)
    return c

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        print(result)
