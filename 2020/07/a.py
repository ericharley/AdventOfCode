import re
from collections import defaultdict

E = defaultdict(list)
W = {}

for line in open('input.txt'):
  parent = line.split(' bags contain ')[0]
  for w,child in re.findall(r'(\d+) ([\w ]+) bag', line):
    E[parent] += [child]
    W[parent,child] = int(w)

V = set(E.keys())

# Part 1
def is_reachable(a,b):
  if a == b:
    return True
  return any(is_reachable(n,b) for n in E[a])

print( sum(is_reachable(v,'shiny gold') for v in V if v != 'shiny gold'))

# Part 2
def weigh(n):
  s = 1
  for nxt in E[n]:
    w = W[n,nxt]
    s += w*weigh(nxt)
  return s

print(weigh('shiny gold') - 1)
