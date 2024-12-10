
class CPU:
  HALT = -1
  INF = 0

  def __init__(self, code):
    self.mem = {}
    self.code = code.copy()
    self.reset()

  def reset(self):
    self.acc = 0
    self.pc = 0
    for i,ins in enumerate(self.code):
      self.mem[i] = ins
  
  def run(self):
    h = {}
    while self.pc < len(self.mem) and self.pc not in h:
      h[self.pc] = 1
      op,val = self.mem[self.pc]
      if op == 'jmp':
        self.pc += val
        continue
      elif op == 'acc':
        self.acc += val

      self.pc += 1

    if self.pc >= len(self.mem):
      return CPU.HALT, self.acc
    else:
      return CPU.INF, self.acc

  def flip(self,i):
    op,val = self.mem[i]
    if op == 'jmp':
      self.mem[i] = 'nop',val
    elif op == 'nop':
      self.mem[i] = 'jmp',val

lines = open('input.txt').read().strip().split('\n')

code = []
for i,line in enumerate(lines):
  op,val = line.split(' ')
  val = int(val)
  code.append((op,val))

cpu = CPU(code)

# Part 1
code, acc = cpu.run()
print(acc)

# Part 2
for i in range(len(cpu.code)):
  cpu.reset()
  cpu.flip(i)
  code,acc = cpu.run()
  if code == CPU.HALT:
    print(acc)
    break
