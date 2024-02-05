from collections import defaultdict

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

p = {
'addr' : 'r[{C}] = r[{A}] + r[{B}]',
'addi' : 'r[{C}] = r[{A}] + {B}',
'mulr' : 'r[{C}] = r[{A}] * r[{B}]',
'muli' : 'r[{C}] = r[{A}] * {B}',
'banr' : 'r[{C}] = r[{A}] & r[{B}]',
'bani' : 'r[{C}] = r[{A}] & {B}',
'borr' : 'r[{C}] = r[{A}] | r[{B}]',
'bori' : 'r[{C}] = r[{A}] | {B}',
'setr' : 'r[{C}] = r[{A}]',
'seti' : 'r[{C}] = {A}',
'gtir' : 'r[{C}] = 1 if {A} > r[{B}] else 0',
'gtri' : 'r[{C}] = 1 if r[{A}] > {B} else 0',
'gtrr' : 'r[{C}] = 1 if r[{A}] > r[{B}] else 0',
'eqir' : 'r[{C}] = 1 if {A} == r[{B}] else 0',
'eqri' : 'r[{C}] = 1 if r[{A}] == {B} else 0',
'eqrr' : 'r[{C}] = 1 if r[{A}] == r[{B}] else 0',
}
data = open('input.txt').read().strip().splitlines()

line = data.pop(0)
pc = int(line.replace('#ip ',''))

program = ['']*len(data)
for i,line in enumerate(data):
  op,A,B,C = line.split()
  A,B,C = map(int,[A,B,C])
  program[i] = (op,A,B,C)

reg = [1,0,0,0,0,0]

#for i in range(len(program)):
#  op,A,B,C = program[i]
#  print(i, p[op].format(A=A,B=B,C=C))

c = defaultdict(int)
while 0 <= reg[pc] < len(program):
  print(reg[pc])
  if reg[pc] == 2 and reg[4] != 0:
    r0, r1, r2, r3, r4, r5 = reg
    while r4 <= r2:
      if r2 % r4 == 0:
        r0 += r4
      r4 += 1
    reg = [r0, r1, r2, r3, r4, r5]
    reg[pc] = 13
    continue

  op,A,B,C = program[reg[pc]]
  reg[C] = ops[op](reg, A, B)
  reg[pc] += 1

  #if reg[pc] == 35:
  #  print(reg)

print(reg)
