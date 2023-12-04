from collections import defaultdict

# read data
filename = 'input.txt'
lines = [line for line in open(filename).read().splitlines()]

# weights
w = defaultdict(lambda : 0)
# card counts
c = defaultdict(lambda : 0)
# score for part 1
total = 0


for line in lines:
  line = line.split()
  pipe_idx = line.index('|')
  max_n = pipe_idx - 2 # how many winning numbers do cards have?
  k = int(line[1][:-1]) # take off the trailing ':'
  a = set([int(x) for x in line[2:(pipe_idx)]]) # winning numbers
  b = set([int(x) for x in line[(pipe_idx+1):]])# revealed numbers
  n = len(a & b) # how many revealed numers are winning

  # Part 1
  total += round(2**(n-1)) # NB: python rounds 0.5 to 0, so works for when n = 0

  # Part 2
  for i in range(1, n+1):
    w[(k,k+i)] += 1

  c[k] = 1
  for i in range(1,max_n+1):
    c[k] += w[(k-i,k)]*c[k-i]


print(total)
print(sum(c.values()))
