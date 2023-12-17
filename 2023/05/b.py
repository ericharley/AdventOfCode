seeds, *blocks = open('input.txt').read().split("\n\n")

seeds = list(map(int, seeds.split(":")[1].split()))

bb = []
for k,block in enumerate(blocks):
   ranges = []
   for line in block.splitlines()[1:]:
     ranges.append( list(map(int, line.split())) )
   bb.append(ranges)

bb.reverse()

def map_location(x):
  # we're going to map each location back through the blocks
  for ranges in bb:
    for b,a,c in ranges:    # swap source / destination meanings
        if b <= x < b + c:
          x = x + a - b
          break
  return x

seeds = list(zip(seeds[::2], seeds[1::2]))

def seed_in_input(seed_num):
  for a,b in seeds:
    if a <= seed_num <= a + b:
      return True
  return False

for location in range(10**9):
  seed_num = map_location(location)
#  if seed_num % 10**5 == 0:
#    print('.', end='')
  if seed_in_input(seed_num):
    print(location)
    break
