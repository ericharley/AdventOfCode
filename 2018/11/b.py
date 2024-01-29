import math
from collections import defaultdict

serial_no = int(open('input.txt').read().strip())

def f(serial_number, x, y):
    rack_id = x + 10
    power_level = (rack_id * y + serial_number)*rack_id
    power_level = (power_level // 100) % 10 - 5
    return power_level

# https://en.wikipedia.org/wiki/Summed-area_table
def maxsum_for_width(I, w):
  max_sum, max_x, max_y = -math.inf, -1, -1
  for x in range(1,300-w):
    for y in range(1,300-w):
      A,B,C,D = (x,y),(x+w,y),(x,y+w),(x+w,y+w)
      isum = I[D] - I[B] - I[C] + I[A]
      if isum > max_sum:
        max_sum = isum
        max_x = x + 1
        max_y = y + 1

  return max_sum, max_x, max_y

I = defaultdict(int)
for x in range(1,300+1):
  for y in range(1,300+1):
    I[x,y] = f(serial_no,x,y) + I[x,y-1] + I[x-1,y] - I[x-1,y-1]

# Part 1
maxsum, max_x, max_y = maxsum_for_width(I,w=3)
print(max_x, max_y)

# Part 2
for s,x,y in [maxsum_for_width(I,w) for w in range(1,300+1)]:
  if s > maxsum:
    maxsum, max_x, max_y = s,x,y
print(max_x, max_y)
