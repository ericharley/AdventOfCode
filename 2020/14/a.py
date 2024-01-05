mem_1 = {}
mem_2 = {}

def update_1(addr, val, mask, mem):
  val = list('{0:036b}'.format(val))
  for i,v in enumerate(mask):
    if v in '01':
      val[i] = v
  val = ''.join(val)
  val = int(val, 2)
  mem[addr] = val

def update_2(addr, val, mask, mem):
  def f(s):
    if 'X' not in s:
      return [s]
    else:
      idx = s.index('X')
      return f(s[0:idx] + '0' + s[idx+1:]) + f(s[0:idx] + '1' + s[idx+1:])

  addr = list('{0:036b}'.format(addr))
  for i,v in enumerate(mask):
     if v == '1':
       addr[i] = '1'
     if v == 'X':
       addr[i] = 'X'
  addr = ''.join(addr)
  for a in f(addr):
    a = int(a, 2)
    mem[a] = val

lines = open('input.txt').read().strip().split('\n')

for line in lines:
 if 'mask' in line:
  mask = line.split(' = ')[1]
 elif 'mem' in line:
  addr, val = line.split(' = ')
  addr = addr.replace('mem[','')
  addr = addr.replace(']','')
  addr = int(addr)
  val = int(val)

  update_1(addr, val, mask, mem_1)
  update_2(addr, val, mask, mem_2)

 else:
  print('error')

# Part 1
print(sum([v for v in mem_1.values()]))

# Part 2
print(sum([v for v in mem_2.values()]))
