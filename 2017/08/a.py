lines = open('input.txt').read().strip().split('\n')
from collections import defaultdict

r = defaultdict(int)
max_r = 0
prog = ''
for line in lines:
  line = line.replace('if ', 'if r["')
  line = line.replace(' >', '"] >')
  line = line.replace(' <', '"] <')
  line = line.replace(' =', '"] =')
  line = line.replace(' !', '"] !')
  f = line.split()
  reg,op,v,cond = f[0],f[1],int(f[2]),' '.join(f[3:])

  prog += f'{cond}:\n'
  prog += f'  r["{reg}"]' + (' += ' if op == 'inc' else '-= ') + f'{v}\n'
  prog += f'  max_r = max(max_r,max(r.values()))\n'

exec(prog)

# Part 1
print(max(r.values()))

# Part 2
print(max_r)

