from collections import defaultdict

filename = 'input.txt'
M = 2503

lines = open(filename).read().strip().split('\n')

reindeer = {}

for line in lines:
  fields = line.split(' ')
# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
  a = fields[0] # Comet
  v = int(fields[3]) # 14
  g = int(fields[6]) # 10
  r = int(fields[13]) # 127
  reindeer[a] = (v,g,r)

#t = defaultdict(list)
#pos = defaultdict(int)
#points = defaultdict(int)
#
#for name in reindeer:
#  b,c,d = reindeer[name]
#  for i in range(c):  # Fly
#    t[name].append(b)
#  for i in range(d):  # Rest
#    t[name].append(0)
#
#for i in range(M):    # Race
#
#  for name in reindeer:
#    N = len(t[name])
#    pos[name] += t[name][i % N]
#
#  lead = max(pos[name] for name in reindeer)
#
#  for name in reindeer:
#    if pos[name] == lead:
#      points[name] += 1
#
## Part 1
#print(max(pos.values()))
## Part2
#print(max(points.values()))

def pos(name,time):
  speed, travel, rest = reindeer[name]
  q, r = divmod(time, travel + rest)
  dist = (q*travel + min(r, travel)) * speed
  return dist

# Part 1

print( max([pos(name, M) for name in reindeer]) )

# Part 2

points = defaultdict(int)

for i in range(1,M+1):    # Race
  lead = max([pos(name,i) for name in reindeer])
  for name in reindeer:
    if pos(name,i) == lead:
      points[name] += 1

print(max(points.values()))
