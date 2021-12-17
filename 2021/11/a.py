import numpy as np
import itertools

a = np.genfromtxt("input.txt", dtype=int, delimiter=1)

total = 0

def step(input):
  global total
  has_flashed = np.zeros(np.shape(input), dtype=bool)

  # First, the energy level of each octopus increases by 1.
  input = input + 1

  while np.any(input > 9):
    # any octopus with an energy level greatter than 9 flashes
    # This process continues as long as new octopuses keep having their energy level 
    # increased beyond 9. (An octopus can only flash at most once per step.)
    for x,y in itertools.product(range(np.shape(a)[0]), range(np.shape(a)[1])):
      if input[x,y] > 9:
          total += 1
          # input[x,y] has a value greater than 9 so it's going to flash
          # NB: (An octopus can only flash at most once per step.)
          has_flashed[x,y] = True
          input[x,y] = 0
          # This increases the energy level of all adjacent octopuses by 1, including 
          # octopuses that are diagonally adjacent.
          for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
              if not ( dx == 0 and dy == 0 ) and (x + dx >= 0 and y + dy >=0): 
                  try:
                    input[x + dx, y + dy] += 1
                  except IndexError as e:
                    pass
  #end while
  output = np.copy(input)
  output[has_flashed] = 0
  return(output)


# Part 1
part1 = np.copy(a)
total = 0
for n in range(0,100):
 part1 = step(part1)
print(total)

#  Part 2
n = 0
part2 = np.copy(a)
while not np.all(part2==0):
  part2 = step(part2)
  n += 1
print(n)
