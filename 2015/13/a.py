import itertools

lines = open('input.txt').read().strip().split('\n')
dist = {}
guests = set()

for line in lines:
  # Alice would gain 54 happiness units by sitting next to Bob.
  fields = line.split(' ')
  a = fields[0] # Alice
  b = fields[-1][0:-1] # Bob
  s = fields[2] # gain
  v = int(fields[3]) # 54
  if s == 'lose':
    v = -v
  dist[a,b] = v
  guests.add(a)
  guests.add(b)

def f(guests, dist):
  max_d = 0

  for path in itertools.permutations(guests):
    d = sum(dist[a,b]+dist[b,a] for a,b in zip(path, path[1:]))
    a,b = path[-1],path[0]
    d += dist[a,b] + dist[b,a]
    max_d = max(d,max_d)

  return max_d

print(f(guests, dist))

guests.add('Me')
for a in guests:
  dist['Me',a] = 0
  dist[a,'Me'] = 0

print(f(guests, dist))
