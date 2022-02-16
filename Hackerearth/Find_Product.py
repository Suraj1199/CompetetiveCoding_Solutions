n = int(input())
prod = 1
for i in map(int, input().split(" ")):
  prod = (prod * i) % 1000000007
print(prod)
