# the board
b = set()

abyss = 0

for line in open(0):
 x = list(map(lambda x : list(map(int,x.split(','))), line.rstrip().split(' -> ')))
 for (x1,y1),(x2,y2) in zip(x, x[1:]):
   x1, x2 = sorted([x1, x2])
   y1, y2 = sorted([y1, y2])
   for x in range(x1, x2+1):
     for y in range(y1, y2 + 1):
       b.add( (x,y) )
       abyss = max(abyss, y+1) # track the largest y value seen so far...

abyss += 1

#print(sorted(b))
#print(abyss)
#print(len(b))

for x in range(-200, 200+1):
  b.add( (x + 500, abyss) )

# how much sand has come through
t = 0

# sand is pouring in from point 500,0
# run the simulation until the sand gets to the abyss y level
while True:
  # starting point
  x = 500
  y = 0
  # fall down one unit if possible until comes to rest.
  while True:
    #print(x,y)
 
    # check if can move down
    # can move down if (x,y+1) NOT in set b
    if (x, y+1) not in b:
      x  = x
      y += 1
      continue
 
    # if can't move down, check if can move left
    if (x-1,y+1) not in b:
      x  = x-1
      y += 1
      continue
 
    # if can't move down or left, check if can move right
    if (x+1,y+1) not in b:
      x  = x+1
      y += 1
      continue
 
    # if can't move down or left or right, settle at current point UNLESS we're at the origin
    if x == 500 and y == 0:
      print(t+1)
      exit(0)
    else:
      b.add( (x,y) )
      t += 1 # sand settled
      break
