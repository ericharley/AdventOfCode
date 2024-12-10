lines = list(map(int,open('input1.txt').readlines()))
d = {x : 2020-x for x in lines}
for x in d:
  if d[x] in d:
    print(x*d[x])
    break

for x in d:
  for y in d:
    if 2020-x-y in d:
      print(x*y*(2020-x-y))
      exit()
