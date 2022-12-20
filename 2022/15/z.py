from z3 import If, Solver, Int
from collections import namedtuple

Sensor = namedtuple("Sensor", "x y")
Beacon = namedtuple("Beacon", "x y")

def abs(x):
  return If(x >= 0, x, -x)

def manhattan_dist(s,b):
  return abs(s.x - b.x) + abs(s.y - b.y)

input = []
# read the input
for line in open(0):
  sx = int(line.split()[2][2:-1])
  sy = int(line.split()[3][2:-1])
  bx = int(line.split()[8][2:-1])
  by = int(line.split()[9][2:])

  sensor = Sensor(sx,sy)
  beacon = Beacon(bx,by)
  d = manhattan_dist(sensor, beacon)
  input.append( (sensor, beacon, d) )

s = Solver()

# what we're solving for
distress_x = Int('x')
distress_y = Int('y')

# box constraints
upper_bound = 4_000_000
lower_bound = 0

s.add(lower_bound <= distress_x)
s.add(distress_x <= upper_bound)

s.add(lower_bound <= distress_y)
s.add(distress_y <= upper_bound)

# the distress signal cannot be the closest beacon to any sensor
for ss, beacon, d in input:
  s.add( manhattan_dist(ss, Beacon(distress_x, distress_y)) > d )

solution = Int('solution')
s.add(solution == distress_x * 4000000 + distress_y)

s.check()
m = s.model()
print('model', m)
