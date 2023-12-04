import sys

m = {'zero'   : 'z0o',
    'one'     : 'o1e',
    'two'     : 't2o',
    'three'   : 't3e',
    'four'    : 'f4r',
    'five'    : 'f5e',
    'six'     : 's6x',
    'seven'   : 's7n',
    'eight'   : 'e8t',
    'nine'    : 'n9e'}

def f(line, m):
  for i, name in enumerate(m.keys()):
    line = line.replace(name, m[name])
  n = ''.join([x for x in line if x.isdigit()])
  return int(n[0] + n[-1])

total1 = 0
total2 = 0

for line in sys.stdin.read().splitlines():
  total1 += f(line, {})
  total2 += f(line, m)

print(total1, total2)
