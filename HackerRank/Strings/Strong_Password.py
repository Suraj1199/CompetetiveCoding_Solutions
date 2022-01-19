def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    up, low, num, sp = 0, 0, 0, 0
    
    for i in range(n):
        if password[i].isnumeric():
            num = 1
        elif password[i].isalpha():
            if password[i].isupper():
                up = 1
            else:
                low = 1
        else:
            sp = 1
    return max(6 - n, 4 - (low + up + sp + num))
            
            
if __name__ == '__main__':
    n = int(input().strip())
    password = input()
    answer = minimumNumber(n, password)
    print(answer)
