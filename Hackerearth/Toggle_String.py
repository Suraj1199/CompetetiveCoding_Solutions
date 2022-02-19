a = ''
for i in input():
  if i.isupper():
    a += i.lower()
  else:
    a += i.upper()
print(a)
