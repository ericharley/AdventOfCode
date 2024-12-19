from functools import cache

lines = open('input.txt').read().strip().split('\n\n')
patterns, data = tuple(lines[0].split(', ')), lines[1].split('\n')

@cache
def f(towel, patterns):
  if towel == '': return 1
  return sum(f(towel.removeprefix(p), patterns) for p in patterns if towel.startswith(p))

# Part 1
print( sum(1 for towel in data if f(towel, patterns) > 0) )

# Part 2
print( sum(f(towel, patterns) for towel in data if f(towel, patterns) > 0) )

