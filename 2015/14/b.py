from collections import defaultdict

filename = 'input.txt'
M = 2503

lines = open(filename).read().strip().split('\n')

reindeer = {}
t = defaultdict(list)
x = defaultdict(int)

for line in lines:
  fields = line.split(' ')
# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
  a = fields[0] # Comet
  b = int(fields[3]) # 14
  c = int(fields[6]) # 10
  d = int(fields[13]) # 127
  reindeer[a] = (b,c,d)

for name in reindeer:
  b,c,d = reindeer[name]
  for i in range(c):
    t[name].append((b,1))
  for i in range(d):
    t[name].append((0,1))

points = defaultdict(int)

for i in range(M):
  for name in reindeer:
    N = len(t[name])
    dx, dt = t[name][i % N]
    x[name] += dx
  lead = max(x[name] for name in reindeer)
  for name in reindeer:
    if x[name] == lead:
      points[name] += 1

print(points)
  
