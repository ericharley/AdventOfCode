from collections import defaultdict

grid = open('input.txt').read().strip().split('\n')

lights = set()

for r in range(len(grid)):
 for c in range(len(grid[0])):
   if grid[r][c] == '#':
     lights.add((r,c))

num_steps = 100

for i in range(num_steps):
  #print(i,len(lights))

  ct = defaultdict(int)
  for r,c in lights:
    ct[r,c] -= 1
    for dr in [-1,0,+1]:
      for dc in [-1,0,+1]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            ct[nr,nc] += 1
        
  new_lights = set()
  
  for light in lights:
    if ct[light] == 2 or ct[light] == 3:
      new_lights.add(light)
 
  for light in ct:
    if ct[light] == 3 and light not in lights:
      new_lights.add(light)

  lights = new_lights

print(len(lights))

