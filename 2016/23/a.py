def print_mem(pc,mem,r):
 print('PC = ', pc, r)
 for i,ins in enumerate(mem):
   print(i,ins)

seen = {}

from collections import defaultdict
count = defaultdict(int)

def do(r):
  pc = 0
  lines = open('input.txt').read().strip().split('\n')
  mem = [0]*len(lines)

  for i,line in enumerate(lines):
    fields = line.split()
    op = fields[0]
    x = fields[1]
    if len(fields) == 3:
      y = fields[2]
    else:
      y = '_'
    mem[i] = (op,x,y)

  seen[tuple(mem)] = 1

  pc = 0
  while pc < len(mem):
    count[pc] += 1
    #print_mem(pc,mem,r)

    (op,x,y) = mem[pc]
    if op == 'cpy':
      if y in 'abcd':
        if x in 'abcd':
          r[y] = r[x]
        else:
          r[y] = int(x)
    elif op == 'inc':
      if x in 'abcd':
        r[x] += 1
    elif op == 'dec':
      if x in 'abcd':
        r[x] -= 1
    elif op == 'tgl':
      if 0 <= pc+r[x] < len(mem):
        (opp,xp,yp) = mem[pc+r[x]]
        if yp == '_':
          if opp == 'inc':
            opp = 'dec'
          else:
            opp = 'inc'
        else:
          if opp == 'jnz':
            opp = 'cpy'
          else:
            opp = 'jnz'
        
        mem[pc+r[x]] = (opp,xp,yp)
        seen[tuple(mem)] = 1
      else:
        1
    elif op == 'jnz':
      if y in 'abcd':
         y = r[y]
      if x in 'abcd':
        if r[x] != 0:
          pc += int(y)
          continue
      else:
        if int(x) != 0:
          pc += int(y)
          continue
    pc += 1
  print(r)

import time
for i in range(6,9+1):
  t0 = time.time()
  do({'a':i,'b':0,'c':0,'d':0})
  t1 = time.time()
  print(i,t1-t0,len(seen))

do({'a':7,'b':0,'c':0,'d':0})

#do({'a':0,'b':0,'c':1,'d':0})
for i in sorted(count.keys()):
 print(i, count[i])
