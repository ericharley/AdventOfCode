from collections import defaultdict

#filename = 'test.txt'
filename = 'input.txt'

instructions, _ = open(filename).read().split('\n\n')
instructions = instructions.split('\n')

edges = defaultdict(lambda: []) 

for s in instructions:
  rule_name = s.split('{')[0]
  rule_list = s.split('{')[1].split(',')[:-1]
  otherwise = s.split('{')[1].split(',')[-1][:-1]

  misc = []
  for rule in rule_list:
    r, go = rule.split(':')
    var,op,val = r[0],r[1],r[2:]

    misc_str = ''
    if len(misc) > 0:
      misc_str = ' and ' + ' and '.join(misc)

    edges[rule_name].append((go,f'({var} {op} {val})' + misc_str))

    not_op = '>=' if op == '<' else '<='
    misc.append(f'({var} {not_op} {val})')

  edges[rule_name].append((otherwise,' and '.join(misc)))


def visitAllPaths(start, dest, condition, path):
  path.append(condition)

  if start == dest:
    yield(' and '.join(path[1:]))
  else:
    for neighbor, new_condition in edges[start]:
        yield from visitAllPaths(neighbor, dest, new_condition, path)

  path.pop()

def intersect_intervals(a, b):
  return (max(a[0],b[0]), min(a[1],b[1]))

def f(op, number):
  if op == '>':
    return (number+1, 4000)
  elif op == '>=':
    return (number, 4000)
  elif op == '<':
    return (1, number-1)
  elif op == '<=':
    return (1, number)

def g(h):
  t = 1
  for v in h:
    t *= (h[v][1] - h[v][0] + 1)
  return t

total = 0
for s in visitAllPaths('in', 'A', '', []):
  h = { key : (1,4000) for key in 'xmas' }
  for v in s.split(' and '):
    var, op, number = v.split(' ')
    var = var[1:]
    number = int(number[:-1])
    h[var] = intersect_intervals(h[var], f(op, number))
  total += g(h)

print(total)
