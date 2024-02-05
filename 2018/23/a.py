lines = open('input.txt').read().strip().splitlines()

nanobots = {}

for line in lines:
  line = line.replace('<','(').replace('>',')')
  line = line.replace(', ','\n')
  exec(line) 

  nanobots[pos] = r

max_r = 0
for pos in nanobots:
  r = nanobots[pos]
  if r > max_r:
    max_r = r
    max_pos = pos

def md(p1,p2):
  return sum([abs(a-b) for a,b in zip(p1,p2)])

# Part 1
print(sum([1 for pos in nanobots if md(max_pos, pos) <= max_r]))
