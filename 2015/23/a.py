def loadProgram(lines):
  mem = [0]*len(lines)
  for i,line in enumerate(lines):
    fields = line.replace(',','').split(' ')
    value = ''
    if len(fields) == 2:
      op, reg = fields
    elif len(fields) == 3:
      op, reg, value = fields

    mem[i] = (op,reg,value)

  return mem

def run(r, pc, mem):
  while pc < len(mem):
    op,reg,value = mem[pc]

    if op == 'hlf':
      r[reg] = r[reg]//2
    if op == 'tpl':
      r[reg] = 3*r[reg]
    if op == 'inc':
      r[reg] += 1

    if op == 'jmp':
      pc += int(reg)
      continue
    if op == 'jie':
      if r[reg] % 2 == 0:
        pc += int(value)
        continue
    if op == 'jio':
      if r[reg] == 1:
        pc += int(value)
        continue

    pc += 1

  return pc

lines = open('input.txt').read().strip().split('\n')
mem = loadProgram(lines)

# Part 1
r = {'a':0,'b':0}
run(r, 0, mem)

print(r['b'])


# Part 2
r = {'a':1,'b':0}
run(r, 0, mem)

print(r['b'])

