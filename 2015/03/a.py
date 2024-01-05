filename = 'input.txt'
dirs = open(filename).read().strip()

houses = {}
m = {'>':1,'<':-1,'^':1j,'v':-1j}

x = 0 + 0j
houses[x] = 1

x = 0 + 0j
for dir in dirs[0::2]:
  x += m[dir]
  houses[x] = 1

x = 0 + 0j
for dir in dirs[1::2]:
  x += m[dir]
  houses[x] = 1

print(len(houses))
