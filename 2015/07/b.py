from functools import cache

wire = {}

for line in open('input.txt').read().strip().split('\n'):

  left, right = line.split(' -> ')
  f = left.split()
  for i,v in enumerate(f):
    if v.isdigit():
      f[i] = int(v)

  if len(f) == 1:
    # 1 -> lx
    a, op, b = f[0], 'I', None

  if len(f) == 2:
    # NOT left -> right
    a, op, b = f[1], f[0], None

  if len(f) == 3:
    # a OP b -> right
    a, op, b = f[0], f[1], f[2]

  wire[right] = (op, a, b)

fs = {
  'LSHIFT' : lambda x,y : x << y,
  'RSHIFT' : lambda x,y : x >> y,
  'AND'    : lambda x,y : x & y,
  'OR'     : lambda x,y : x | y,
  'NOT'    : lambda x,y : ~x,
  'I'      : lambda x,y : x,
}

@cache
def g(x):
  if x in wire:
    op, a, b = wire[x]
    return fs[op](g(a),g(b))
  else:
    return x

# Part 1
print(g('a'))

# Part 2
wire['b'] = ('I',g('a'),None)
g.cache_clear()
print(g('a'))
