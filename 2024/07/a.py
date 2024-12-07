lines = open('input.txt').read().splitlines()

data = []
for line in lines:
  a, *ns = list(map(int,line.replace(':','').split(' ')))
  data += [(a,ns)]

def solve(data, ops):
  t = 0
  for a,ns in data:
    results = {ns[0]}

    for n in ns[1:]:
      results = {op(x,n) for x in results for op in ops}

    if a in results:
      t += a

  return t

# Part 1
from operator import mul, add
print( solve(data, [mul, add]) )

# Part 2
f = lambda a,b : int(f'{a}{b}')
print( solve(data, [mul, add, f]) )
