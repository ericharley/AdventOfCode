import itertools
lines = open('input.txt').read().strip().split('\n')

vertices = set()
dist = {}

for line in lines:
 a,b,d = line.split(' ')[::2]
 d = int(d)
 vertices.add(a)
 vertices.add(b)
 dist[a,b] = d
 dist[b,a] = d

min_d = 1_000_000
max_d = 0

for path in itertools.permutations(vertices):
  d = sum(dist[a,b] for a,b in zip(path, path[1:]))
  min_d = min(d,min_d)
  max_d = max(d,max_d)

print(min_d, max_d)
