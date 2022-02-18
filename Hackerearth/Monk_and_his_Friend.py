for _ in range(int(input())):
  p, m = map(int, input().split(" "))
  print(bin(p ^ m)[2:].count('1'))
