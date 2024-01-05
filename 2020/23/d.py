cups = list(map(int,'135468729'))
#cups = list(map(int,'389125467'))

cups.extend(range(10, 10**6 + 1))
N = len(cups)

succ = [0] * (N + 1)
for idx, v in enumerate(cups):
  succ[v] = cups[(idx+1) % N]

current_cup = cups[0]

for i in range(10**7):
  a = succ[current_cup]
  b = succ[a]
  c = succ[b]

  dest_cup = (current_cup - 1)
  if dest_cup == 0:
    dest_cup += N
  while dest_cup in [a,b,c]:
    dest_cup = (dest_cup - 1)
    if dest_cup == 0:
      dest_cup += N

  succ[current_cup] = succ[c]
  succ[c] = succ[dest_cup]
  succ[dest_cup] = a

  current_cup = succ[current_cup]

print(succ[1]*succ[succ[1]])

