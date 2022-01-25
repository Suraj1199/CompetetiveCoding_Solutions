def maximumToys(prices, k):
    prices.sort()
    spend = 0
    i = 0
    while spend + prices[i] <= k:
        spend += prices[i]
        i += 1
    return i

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)
