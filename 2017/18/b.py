def run(id, mem, in_queue, out_queue):

  count = 0
  r = {}
  for v in 'abcdefghijklmnopqrstuvwxyz':
    r[v] = 0

  r['p'] = id

  def getVal(A):
    if A in 'abcdefghijklmnopqrstuvwxyz':
      return r[A]
    else:
      return int(A)

  last_freq = 0
  pc = 0
  while 0 <= pc < len(mem):
    op,X,Y = mem[pc]

    if op == 'set':
      r[X] = getVal(Y)

    if op == 'add':
      r[X] = getVal(X) + getVal(Y)

    if op == 'mul':
      r[X] = getVal(X) * getVal(Y)

    if op == 'mod':
      r[X] = getVal(X) % getVal(Y)

    if op == 'snd':
      last_freq = getVal(X)
      out_queue.put(getVal(X))
      count += 1

    if op == 'rcv':
      try:
        r[X] = in_queue.get(timeout=1)
      except queue.Empty:
        return count

    if op == 'jgz':
      if getVal(X) > 0:
        pc += getVal(Y)
        continue  

    pc += 1
  return count

# Parse program
mem = open('input.txt').read().strip().split('\n')

for k,ins in enumerate(mem):
  f = ins.split()
  Y = '_'

  if len(f) == 2:
    op,X = f
  if len(f) == 3:
    op,X,Y = ins.split()

  mem[k] = (op,X,Y)

mem = tuple(mem)

import queue
import multiprocessing.pool

pool = multiprocessing.pool.ThreadPool(processes=2)

q1 = multiprocessing.Queue()
q2 = multiprocessing.Queue()
res1 = pool.apply_async(run, (0, mem, q1, q2))
res2 = pool.apply_async(run, (1, mem, q2, q1))

res1.get()
print(res2.get())


