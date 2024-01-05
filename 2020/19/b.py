filename = 'input2.txt'

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

def p(id,k):
  output = ''

  if k == 0:
    pass

  elif isinstance(f[id], list):
    for v in f[id]:
      output += '(' + p(v,k-1) + ')'

  elif isinstance(f[id], tuple):
    left = f[id][0]
    right = f[id][1]

    output += '('

    for v in left:
      output += '(' + p(v,k-1) + ')'

    output += '|'

    for v in right:
      output += '(' + p(v,k-1) + ')'

    output += ')'

  elif isinstance(f[id], str):
    output += f[id]

  else:
    print('err')
    exit()

  return output

import re
pattern = re.compile('^' + p(0,100) + '$')

print(sum([1 for m in messages if re.match(pattern, m)]))

