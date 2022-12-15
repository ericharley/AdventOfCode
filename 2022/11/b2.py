items = [[91, 54, 70, 61, 64, 64, 60, 85],
         [82],
         [84, 93, 70],
         [78, 56, 85, 93],
         [64, 57, 81, 95, 52, 71, 58],
         [58, 71, 96, 58, 68, 90],
         [56, 99, 89, 97, 81],
         [68, 72]
]
ops = [lambda old : old * 13,
       lambda old : old + 7,
       lambda old : old + 2,
       lambda old : old * 2,
       lambda old : old * old,
       lambda old : old + 6,
       lambda old : old + 1,
       lambda old : old + 8
]

mods = [2,13,5,3,11,17,7,19]
def prod(l):
  if l == []:
    return 1   
  else:
    return l[0] * prod(l[1:])
    
mod = prod(mods)

d = {}
d[0] = {True: 5, False: 2}
d[1] = {True: 4, False: 3}
d[2] = {True: 5, False: 1}
d[3] = {True: 6, False: 7}
d[4] = {True: 7, False: 3}
d[5] = {True: 4, False: 1}
d[6] = {True: 0, False: 2}
d[7] = {True: 6, False: 0}

N = len(items)


class Monkey:
  def __init__(self, items, l, m, t):
    self.items = items
    self.op = l
    self.mod = m
    self.t = t
    self.count = 0

Monkeys = list(range(N))
for i in range(N):
 Monkeys[i] = Monkey(items[i], ops[i], mods[i], d[i])

def print_monkeys():
  for m in range(N):
    M = Monkeys[m]
    print(f'Monkey {m}: {M.items}')
  print()

def print_monkeys_count():
  for m in range(N):
    M = Monkeys[m]
    print(f'Monkey {m} inspected items {M.count} times.')
  print()

for r in range(10000):
  #print(f"Round {r}:")
  #print_monkeys()

  for m in range(N):
    M = Monkeys[m]
    while M.items:
      M.count += 1
      item = M.items.pop(0)
      item = M.op(item) % mod
      Monkeys[M.t[item % M.mod == 0]].items.append(item)

#print(f"Round 20:")
#print_monkeys()

#print_monkeys_count()

l = [ Monkeys[r].count for r in range(N) ]
l.sort()
monkey_business = l[-1]*l[-2]
print(monkey_business)
