from collections import namedtuple

Sensor = namedtuple("Sensor", "x y")
Beacon = namedtuple("Beacon", "x y")

def manhattan_dist(s,b):
  # manhattan distance from sensor to beacon
  d = abs(s.x - b.x) + abs(s.y - b.y)
  return d

input = []

# read the input
for line in open(0):

  sx = int(line.split()[2][2:-1])
  sy = int(line.split()[3][2:-1])
  bx = int(line.split()[8][2:-1])
  by = int(line.split()[9][2:])

  sensor = Sensor(sx,sy)
  beacon = Beacon(bx,by)

  input.append( (sensor,beacon) )

#M = 20
M = 4_000_000

for Y in range(M,-1,-1):
  intervals = []

  for sensor, beacon in input:
    d = manhattan_dist(sensor, beacon)
    r = d - abs(sensor.y - Y)
    if r < 0:
      continue
    intervals.append( (sensor.x - r, sensor.x + r) )

  a = intervals
  b = []
  for begin,end in sorted(a):
    if b and b[-1][1] >= begin - 1:
        b[-1][1] = max(b[-1][1], end)
    else:
        b.append([begin, end])

  if len(b) > 1:
    x = b[0][1]+1
    print(4000000*x + Y)
    exit(0)

#  # all points on line y = 10... (x,10), x = -infinity to infinity...
#  # what are those points that are d units or less to this sensor?
#  # 
#  abs(sx - xx) + abs(sy - y) <= d
#  abs(sx - xx) <= d - abs(sy - y) = r (1)
#    r = d - abs(sy - y)
#    abs(sx - xx) <= r
#=> -r <= (sx - xx) <= r
#=> -r - sx <= -xx <= r - sx
#=>  r + sx >=  xx >= -r + sx
#
#    sx - r <= xx <= sx + r
#
#    if r < 0 then... there are no xx that satisfy equation (1)
#
#    if r == 0
#   
#      sx <= xx <= sx
#      xx == sx
# 
#  r = d - abs(sy - y)
