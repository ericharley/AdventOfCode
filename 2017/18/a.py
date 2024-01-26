mem = open('input.txt').read().strip().split('\n')

from collections import defaultdict
r = {}
for v in range(-20,229749):
  r[v] = v
for v in 'abcdefghijklmnopqrstuvwxyz':
  r[v] = 0

for k,ins in enumerate(mem):
  f = ins.split()

  if len(f) == 2:
    op,X = f
    Y = '_'

  if len(f) == 3:
    op,X,Y = ins.split()
    if Y not in 'abcdefghijklmnopqrstuvwxyz':
      Y = int(Y)

  mem[k] = (op,X,Y)  

last_freq = 0
pc = 0
while 0 <= pc < len(mem):
  op,X,Y = mem[pc]

  if op == 'set':
    r[X] = r[Y]

  if op == 'add':
    r[X] = r[X] + r[Y]

  if op == 'mul':
    r[X] = r[X] * r[Y]

  if op == 'mod':
    r[X] = r[X] % r[Y]

  if op == 'snd':
    last_freq = r[X]

  if op == 'rcv':
    if r[X] != 0:
      print(last_freq)
      break

  if op == 'jgz':
    if r[X] > 0:
      pc += r[Y]
      continue  

  pc += 1
