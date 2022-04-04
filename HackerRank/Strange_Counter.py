from math import ceil
def strangeCounter(t):
    l = len(bin(ceil(t / 3))[2:])
    return 3 * ((1 << l) - 1) - t + 1

if __name__ == '__main__':
    t = int(input().strip())
    result = strangeCounter(t)
    print(result)
