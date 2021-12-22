import re

class Cube:
  def __init__(self, x, y, z, on):
    self.min_x, self.max_x = min(x), max(x)
    self.min_y, self.max_y = min(y), max(y)
    self.min_z, self.max_z = min(z), max(z)
    self.on = on

    self.volume = (self.max_x - self.min_x + 1) * (self.max_y - self.min_y + 1) * (self.max_z - self.min_z + 1)

  def is_small(self):
    return -50 <= min(self.min_x, self.min_y, self.min_z) and 50 >= max(self.max_x, self.max_y, self.max_z)

  def intersect(self, other):
    if self.max_x < other.min_x or self.min_x > other.max_x:
      return None
    if self.max_y < other.min_y or self.min_y > other.max_y:
      return None
    if self.max_z < other.min_z or self.min_z > other.max_z:
      return None

    return Cube(
        (min(self.max_x, other.max_x), max(self.min_x, other.min_x)),
        (min(self.max_y, other.max_y), max(self.min_y, other.min_y)),
        (min(self.max_z, other.max_z), max(self.min_z, other.min_z)),
        other.on if self.on != other.on else not other.on)


def do_volume(regions):
 processed = []
 # Process each cube in order, one at a time
 for region in regions:
 
   next_processed = []
 
   # going over all the previously added cubes
   for prev_region in processed:
     # keep these in order...
     next_processed.append(prev_region)

     # if there's an interesection between the current cube and any previous cube compute the overlap and add it to the list...
     overlap = prev_region.intersect(region)
     if overlap :
       next_processed.append(overlap)
       # the signs work here like this: if there's two on cubes that overlap, then the overlap cube is an off cube so we can add the 
       # volume of the two original cubes and subtract the overlap of the intersection and get the proper union
 
   # if this cube is an on cube, we keep it on the list. otherwise, it's an off cube and it'll have turned off any cubes it 
   # intersects with already
   if region.on:
     next_processed.append(region)
 
   processed = next_processed
 
 print(sum(region.volume if region.on else -region.volume for region in processed))



regions = []
with open('input.txt') as file:
  for line in file.readlines():
     m = re.match(r'^(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)', line.strip())
     status, min_x, max_x, min_y, max_y, min_z, max_z = m.groups()
     regions.append(Cube((int(min_x), int(max_x)), (int(min_y), int(max_y)), (int(min_z), int(max_z)), status == "on"))

do_volume([x for x in regions if x.is_small()])
do_volume(regions)
