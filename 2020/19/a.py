#filename = 'test.txt'
filename = 'input.txt'

rules, messages = open(filename).read().strip().split('\n\n')
rules = rules.split('\n')
messages = messages.split('\n')

f = {}

for rule in rules:
  id, r = rule.split(': ')
  id = int(id)

  if '"' in r:
    ch = r.replace('"','')
    f[id] = ch

  elif '|' in r:
    left, right = r.split(' | ')
    left = list(map(int,left.split(' ')))
    right = list(map(int,right.split(' ')))
    
    f[id] = (left,right)

  else:
    f[id] = list(map(int, r.split(' ')))

def p(id):
  output = ''

  if isinstance(f[id], list):
    for v in f[id]:
      output += '(' + p(v) + ')'

  elif isinstance(f[id], tuple):
    left = f[id][0]
    right = f[id][1]

    output += '('

    for v in left:
      output += '(' + p(v) + ')'

    output += '|'

    for v in right:
      output += '(' + p(v) + ')'

    output += ')'

  elif isinstance(f[id], str):
    output += f[id]

  else:
    print('err')
    exit()

  return output

import re
rstr = '^' + p(0) + '$'
pattern = re.compile(rstr)

def valid(m):
  if re.match(pattern, m):
    return True
  else:
    return False

print(sum([1 for m in messages if valid(m)]))
