from collections import namedtuple

Point = namedtuple("Point","x y z")

droplets = set()

file = open("input.txt")
lines = file.readlines()
for line in lines:
  x,y,z = map(int, line.split(','))
  p = Point(x,y,z)
  droplets.add(p)

offsets = [Point(-0.5, 0, 0), Point(0.5, 0, 0), Point(0, -0.5, 0), Point(0, 0.5, 0), Point(0, 0, -0.5), Point(0, 0, 0.5)]

faces = {}
# for each point
for p in droplets:
  for offset in offsets:
    f = Point(p.x + offset.x, p.y + offset.y, p.z + offset.z)
    # count the number of times each face occurs
    if f not in faces:
      faces[f] = 1
    else:
      faces[f] += 1

t = 0

for f in faces:
  if faces[f] == 1:
    t += 1

print(t)
