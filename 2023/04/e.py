from collections import defaultdict

# read data
filename = 'input.txt'
lines = [line for line in open(filename).read().splitlines()]

# card counts
c = defaultdict(int)

# score for part 1
total = 0

for k, line in enumerate(lines):
  _, right = line.split(': ')
  a_str, b_str = right.split(' | ')
  a = set(a_str.split())
  b = set(b_str.split())
  n = len(a & b) # how many revealed numers are winning

  # Part 1
  total += 2**(n-1) if n != 0 else 0

  # Part 2
  c[k] += 1
  for i in range(1,n+1):
    c[k+i] += c[k]

print( total, sum(c.values()) )
