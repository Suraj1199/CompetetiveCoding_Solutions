n, k = map(int, input().split()) 
h = map(int, input().split())
print(max(max(h) - k, 0))
