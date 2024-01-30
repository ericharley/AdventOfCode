one,two = open('input.txt').read().strip().split('\n\n\n\n')
data = one.split('\n\n')
two = two.splitlines()

N = len(data)
before = [0]*N
ins = [0]*N
after = [0]*N
program = ['']*len(two)

for i,block in enumerate(data):
  before[i], ins[i], after[i] = block.split('\n')

  before[i] = before[i].replace('Before: [','').replace(']','')  
  before[i] = list(map(int,before[i].split(',')))
  
  ins[i] = ins[i].replace(' ',',')
  ins[i] = list(map(int,ins[i].split(',')))
  
  after[i] = after[i].replace('After:  [','').replace(']','')  
  after[i] = list(map(int,after[i].split(',')))

for i,line in enumerate(two):
  opc,A,B,C = map(int,line.split())
  program[i] = (opc,A,B,C)


ops = {}
ops['addr'] = (lambda r,A,B : r[A] + r[B])
ops['addi'] = (lambda r,A,B : r[A] + B)
ops['mulr'] = (lambda r,A,B : r[A] * r[B])
ops['muli'] = (lambda r,A,B : r[A] * B)
ops['banr'] = (lambda r,A,B : r[A] & r[B])
ops['bani'] = (lambda r,A,B : r[A] & B)
ops['borr'] = (lambda r,A,B : r[A] | r[B])
ops['bori'] = (lambda r,A,B : r[A] | B)
ops['setr'] = (lambda r,A,B : r[A])
ops['seti'] = (lambda r,A,B : A)
ops['gtir'] = (lambda r,A,B : (1 if A > r[B] else 0))
ops['gtri'] = (lambda r,A,B : (1 if r[A] > B else 0))
ops['gtrr'] = (lambda r,A,B : (1 if r[A] > r[B] else 0))
ops['eqir'] = (lambda r,A,B : (1 if A == r[B] else 0))
ops['eqri'] = (lambda r,A,B : (1 if r[A] == B else 0))
ops['eqrr'] = (lambda r,A,B : (1 if r[A] == r[B] else 0))


# Part 1
t = 0
for i in range(N):
  _,A,B,C = ins[i]
  could_be = sum([(after[i][C] == ops[op](before[i],A,B)) for op in ops])
  if could_be >= 3:
    t+=1
print(t)


# Part 2
possible_opc = {}
for op in ops:
  possible_opc[op] = set(range(0,16))

for i in range(N):
  opc,A,B,C = ins[i]
  for op in ops:
    if not (after[i][C] == ops[op](before[i],A,B)):
      possible_opc[op] -= set([opc])

known = set()
while any([len(possible_opc[op]) > 1 for op in possible_opc]):
  for op in possible_opc:
    if len(possible_opc[op]) == 1:
      known |= possible_opc[op]
      
  for op in possible_opc:
    if len(possible_opc[op]) != 1:
      possible_opc[op] -= known

m = ['']*16
for k,v in possible_opc.items():
  opc = list(v)[0]
  m[opc] = k

reg = [0,0,0,0]
for opc,A,B,C in program:
  reg[C] = ops[m[opc]](reg, A, B)

print(reg[0])