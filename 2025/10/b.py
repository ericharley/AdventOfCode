lines = open('test.txt').read().strip().splitlines()

from collections import defaultdict

print('Total[{')

for j,line in enumerate(lines):
  A = defaultdict(list)
  f = line.split()
  target = f[0].replace('[','').replace(']','')
  buttons = [ (eval(b[:-1]+',)')) for b in f[1:-1]]

  joltages = tuple(eval(f[-1].replace('{','[').replace('}',']')))

  N = len(buttons) # Number of buttons

  vars = set()
  for k,v_k in enumerate(joltages):
    for i,b in enumerate(buttons):
      if k in b:
        A[k].append(i)
        vars.add(i)

  #print(j, len(joltages))
  s = []
  for k in A:
    if k < len(joltages):
      #print(k,A[k],joltages[k])
      s.append( ('+'.join([f'x{x}' for x in A[k]])+'=='+str(joltages[k])) )
  #print(len(A))
  t = ('+'.join([f'x{x}' for x in vars]))

  s = ' && '.join(s)
  q = f"""
Minimize[{{ {t}, {s} }}, {{x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12}}, NonNegativeIntegers][[1]],
"""
  print(q)

print('}]')

# x_i is the number of times we push button i
#
# sum (of buttons x_i that effect joltage k) == v_k
#
# Minmize
#   sum x_i
# subject to
#   sum (of buttons x_i that effect joltage k) == v_k
