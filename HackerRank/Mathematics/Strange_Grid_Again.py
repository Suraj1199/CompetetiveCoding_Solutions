r, c = map(lambda x: int(x) - 1, input().rstrip().split())
print(r // 2 * 10 + 2 * c + r % 2)
