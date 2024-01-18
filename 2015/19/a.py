import re
from collections import defaultdict

data = open('input.txt').read().strip()

rules = [a.split(' => ') for a in data.split('\n\n')[0].split('\n')]

target = data.split('\n\n')[1]
molecule = re.sub(r'([A-Z])',r' \1', target).lstrip().split(' ')

# Part 1
elements = {a for a,b in rules}
rewrite = defaultdict(list)
for r in elements:
  rewrite[r] = [b for a,b in rules if a == r]

output = set()
for i,atom in enumerate(molecule):
  for rule in rewrite[atom]:
    output.add(''.join(molecule[0:i] + [rule] + molecule[i+1:]))

print(len(output))

# Part 2
count = 0
while target != 'e':
  for a, b in rules:
    if b in target:
      target = target.replace(b, a, 1)
      count += 1

print(count)
