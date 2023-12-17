filename = 'input.txt'

grid = tuple(open(filename).read().splitlines())

def cycle():
    global grid
    for _ in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = tuple("#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in grid)
        grid = tuple(row[::-1] for row in grid)

def calc_load():
  return sum([row.count("O")*(len(grid) - r) for r,row in enumerate(grid)])


T = 10**9
cycle_count = 0

seen = {}

while cycle_count < T:
  # we're at a place we have been before
  if grid in seen:
    last_count = seen[grid] # cycle count when we were here
    cycle_length = cycle_count - last_count
    rem = T - cycle_count  # how many more do we have to go
    rep = rem // cycle_length

    cycle_count += rep*cycle_length
    break

  seen[grid] = cycle_count
  cycle()
  cycle_count+=1

# finish it out
while cycle_count < T:
  cycle()
  cycle_count+=1

print(calc_load())
