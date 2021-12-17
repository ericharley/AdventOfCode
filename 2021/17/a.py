def sign(x):
  if x < 0:
    return -1
  if x > 0:
    return +1
  return 0

def step(x, v):
  x[0] += v[0]
  x[1] += v[1]
  # decrease velocity
  v[0] -= sign(v[0])
  v[1] -= 1

def in_target(x, target):
  if target['x']['lower'] <= x[0] <= target['x']['upper']:
    if target['y']['lower'] <= x[1] <= target['y']['upper']:
      return True
  return False

# target area: x=111..161, y=-154..-101
target = { 'x':{}, 'y':{} }
target['x']['lower'] = 20
target['x']['upper'] = 30
target['y']['lower'] = -10
target['y']['upper'] = -5


for vx in range(1,1000,1):
 for vy in range(-1000,1000,1):
  #vx = 6
  #vy = 3
  x = [0,0]
  v = [vx,vy]

  i = 0

  #print(f'x[{i}]', x)

  stop = False
  while not stop:
    i+=1
    xprev = x.copy()
    step(x,v)
    if in_target(x,target):
       stop = True
       print('v[0]', [vx,vy])
       break
    if x[1] < target['y']['lower'] and (xprev[0] - x[0]) == 0:
       #print('no hit')
       stop = True
       break
    #print(f'x[{i}]', x)



# observations: the x position is going to hit a wall and stop changing, 
# and then the y position is going to drop.
# stop iterating when x is unchanging AND y is below the target
