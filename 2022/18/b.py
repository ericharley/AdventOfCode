from collections import deque
from collections import namedtuple

Point = namedtuple("Point","x y z")

droplets = set()

min_x = 1000
min_y = 1000
min_z = 1000

max_x = -1000
max_y = -1000
max_z = -1000

file = open("input.txt")
lines = file.readlines()
for line in lines:
  x,y,z = map(int, line.split(','))
  p = Point(x,y,z)
  droplets.add(p)
  min_x = min(min_x, x)
  max_x = max(max_x, x)
  min_y = min(min_y, y)
  max_y = max(max_y, y)
  min_z = min(min_z, z)
  max_z = max(max_z, z)

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
# surface area faces are those that are only counted once
for f in faces:
  if faces[f] == 1:
    t += 1
print(t)


# Part 2
external = set()
bounding_cube = set()

for x in range(min_x-1, max_x+1 + 1):
 for y in range(min_y-1, max_y+1 + 1):
  for z in range(min_z-1, max_z+1 + 1):
    bounding_cube.add(Point(x,y,z))

# only have to classify the points that aren't droplets inside the bounding cube.
bounding_cube = bounding_cube - droplets


# I know this point is external
e = Point(min_x-1,min_y-1,min_z-1)
d = deque()
d.append(e)

def cube_neighbors(p):
  l = []
  offsets = [Point(-1, 0, 0), Point(1, 0, 0), Point(0, -1, 0), Point(0, 1, 0), Point(0, 0, -1), Point(0, 0, 1)]
  for offset in offsets:
    n = Point(p.x + offset.x, p.y + offset.y, p.z + offset.z)
    if n in bounding_cube:
      l.append(n)
  return l


while d:
  curr_point = d.pop()
  external.add(curr_point)
  for neighbor in cube_neighbors(curr_point):
    if neighbor not in external:
      d.append(neighbor)


offsets = [Point(-0.5, 0, 0), Point(0.5, 0, 0), Point(0, -0.5, 0), Point(0, 0.5, 0), Point(0, 0, -0.5), Point(0, 0, 0.5)]
external_faces = set()
# for each point
for p in external:
  for offset in offsets:
    f = Point(p.x + offset.x, p.y + offset.y, p.z + offset.z)
    external_faces.add(f)  

t = 0
for p in droplets:
  for offset in offsets:
    f = Point(p.x + offset.x, p.y + offset.y, p.z + offset.z)
    if f in external_faces:
      t += 1
   
print(t)
