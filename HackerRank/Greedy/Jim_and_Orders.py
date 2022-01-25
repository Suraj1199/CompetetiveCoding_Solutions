def jimOrders(orders):
    for i in range(len(orders)):
        orders[i].append(i + 1)
    return [i for _, _, i in sorted(orders, key=lambda x : x[0] + x[1])]

if __name__ == '__main__':
    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)
    print(result)
