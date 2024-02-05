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

data = open('input.txt').read().strip().splitlines()

line = data.pop(0)
pc = int(line.replace('#ip ',''))

program = ['']*len(data)
for i,line in enumerate(data):
  op,A,B,C = line.split()
  A,B,C = map(int,[A,B,C])
  program[i] = (op,A,B,C)

reg = [0,0,0,0,0,0]

while 0 <= reg[pc] < len(program):
  op,A,B,C = program[reg[pc]]
  reg[C] = ops[op](reg, A, B)
  reg[pc] += 1

print(reg)
