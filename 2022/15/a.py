from collections import namedtuple

Sensor = namedtuple("Sensor", "x y")
Beacon = namedtuple("Beacon", "x y")

beacons = set()
sensors = set()

nope = set()

y = 2000000
#y = 10

# read the input
for line in open(0):

  sx = int(line.split()[2][2:-1])
  sy = int(line.split()[3][2:-1])
  bx = int(line.split()[8][2:-1])
  by = int(line.split()[9][2:])

  # manhattan distance from sensor to beacon
  d = abs(sx - bx) + abs(sy - by)

  sensor = Sensor(sx,sy)
  beacon = Beacon(bx,by)

  beacons.add(beacon)
  sensors.add(sensor)

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
  r = d - abs(sy - y)
  for xx in range(sx-r, sx+r + 1):
    # the point at (xx, y) cannot have a beacon in it:
    # lots of duplicate work here with overlapping intervals
    nope.add( Beacon(xx,y) )    

#  print(line)
#  print(sensor, beacon)

print(len(nope - beacons))
