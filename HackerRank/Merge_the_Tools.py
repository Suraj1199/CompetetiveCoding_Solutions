def merge_the_tools(string, k):
    n_sub = int(len(string)/k)
    for i in range(n_sub):
        sub = string[i*k : (i+1)*k]
        sub_uniq = list(dict.fromkeys(list(sub)))
        print("".join(sub_uniq))
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
