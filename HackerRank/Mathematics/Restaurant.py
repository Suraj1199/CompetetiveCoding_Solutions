def restaurant(l, b):
    if l > b:
        l, b = b, l
    def hcf(x, y):
        if y % x == 0:
            return x
        return hcf(y % x, x)
    h = hcf(l, b)
    return l // h * b // h
        
if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        l = int(first_multiple_input[0])
        b = int(first_multiple_input[1])

        result = restaurant(l, b)
	print(result)
