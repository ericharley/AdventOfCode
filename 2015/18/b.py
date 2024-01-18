from collections import defaultdict

grid = open('input.txt').read().strip().split('\n')
corners = { (0,0), (0,len(grid[0])-1), (len(grid)-1,0), (len(grid)-1,len(grid[0])-1) }

lights = set()

for r in range(len(grid)):
 for c in range(len(grid[0])):
   if grid[r][c] == '#':
     lights.add((r,c))


lights = lights | corners

num_steps = 100

def neighbors(r,c):
  for dr in [-1,0,+1]:
    for dc in [-1,0,+1]:
      if (r+dr,c+dc) != (r,c):
        if 0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[0]):
          yield (r+dr,c+dc)

for i in range(num_steps):

  ct = defaultdict(int)
  for r,c in lights:
    for nr,nc in neighbors(r,c):
      ct[nr,nc] += 1
        
  new_lights = set()
  
  for light in lights:
    if ct[light] == 2 or ct[light] == 3:
      new_lights.add(light)
 
  for light in ct:
    if ct[light] == 3 and light not in lights:
      new_lights.add(light)

  lights = new_lights | corners

print(len(lights))

