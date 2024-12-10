from collections import Counter
from functools import cache

d = list(map(int,open('input.txt').readlines()))
max_output = max(d)+3
d = sorted([0,max_output] + d)

# Part 1
c = Counter([d[i+1]-d[i] for i in range(len(d)-1)])
print(c[1]*c[3])

@cache
def f(i):
# how many ways to get to i
  if i < 0:
    return 0
  if i == 0:
    return 1
  return (i-1 in d)*f(i-1) + (i-2 in d)*f(i-2) + (i-3 in d)*f(i-3)

print(f(max_output))
