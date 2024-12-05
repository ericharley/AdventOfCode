from functools import cmp_to_key

rules,runs = open('input.txt').read().strip().split('\n\n')
rules = {tuple(map(int,x.split('|'))) for x in rules.split()}
runs  = {tuple(map(int,x.split(','))) for x in runs.split()}

def is_valid(ps):
  return all(ps.index(a) < ps.index(b) for a,b in rules if a in ps and b in ps)

def median(ps):
  return ps[(len(ps) - 1) // 2]

# Part 1
valid = {ps for ps in runs if is_valid(ps)}
print( sum(median(x) for x in valid) )

# Part 2
invalid = runs - valid
cmp = lambda p,q : -1 if (p,q) in rules else +1
print( sum(median(sorted(x, key=cmp_to_key(cmp))) for x in invalid) )
