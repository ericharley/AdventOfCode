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

  pc = 0
  while pc < len(mem):
    (op,x,y) = mem[pc]
    if op == 'cpy':
      if x in 'abcd':
        r[y] = r[x]
      else:
        r[y] = int(x)
    elif op == 'inc':
      r[x] += 1
    elif op == 'dec':
      r[x] -= 1

    elif op == 'jnz':
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

do({'a':0,'b':0,'c':0,'d':0})
do({'a':0,'b':0,'c':1,'d':0})

