from collections import namedtuple

Particle = namedtuple('Particle','p v a id')
Point = namedtuple('Point','x y z')

def manhattan(pnt:Point):
  return sum([abs(v) for v in pnt])

def T(n):
  return n*(n+1)//2

def pos_at(p:Particle, t):
  return Point(*(x0 + v*t + a*T(t) for x0,v,a in zip(p.p, p.v, p.a)))

particles = set()
min_d = -1

lines = open('input.txt').read().strip().splitlines()
for i,line in enumerate(lines):
  line = line.replace('<','Point(').replace('>',')')
  line = line.replace(', ','\n')
  exec(line)

  _p = Particle(p,v,a,i)
  particles.add(_p)

  _d = manhattan(pos_at(_p,t=1000))
  if _d < min_d or min_d == -1:
    min_d, min_id = _d, i

# Part 1
print(min_id)

# Part 2
from collections import defaultdict

for t in range(1, 50):
  space = defaultdict(set)
  for p in particles:
    space[pos_at(p,t)].add(p)

  for colliding_particles in space.values():
    if len(colliding_particles) > 1:
      particles -= colliding_particles

print(len(particles))


