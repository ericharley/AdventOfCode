def print_mem(pc,mem,r):
 print('PC = ', pc, r)
 for i,ins in enumerate(mem):
   print(i,ins)


def do(r):
  output = ''
  seen = {}
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
    key = (pc,tuple(r.items()),tuple(mem))
    if key in seen:
      break
    seen[key] = 1
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
    elif op == 'out':
      output += str(r[x])
    else:
      print('error',op,x,y)
    pc += 1
  return output

for i in range(1000):
  output = do({'a':i,'b':0,'c':0,'d':0})
  if output == '010101010101':
    print(i)
    break
