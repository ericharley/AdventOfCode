filename = 'test.txt'
filename = 'input.txt'

lines = open(filename).read().strip().split('\n')

A = set()
I = set()
for line in lines:
  left, right = line.split(' (contains ')
  ingredients = left.split(' ')
  allergens = right.replace(')','').split(', ')
  I |= set(ingredients)
  A |= set(allergens)

m = { a : set(I) for a in A }

for line in lines:
  left, right = line.split(' (contains ')
  ingredients = left.split(' ')
  allergens = right.replace(')','').split(', ')
  for a in allergens:
    m[a] &= set(ingredients)

# Part 1
x = [m[k] for k in m]
possible = set.union(*x)
impossible = I - possible

t = 0
for i in impossible:
  for line in lines:
    left, right = line.split(' (contains ')
    ingredients = left.split(' ')
    if i in ingredients:
      t += 1
print(t)


# Part 2
to_remove = set()
while any([len(m[ingredient]) > 1 for ingredient in m]):

  for ingredient in m:
    if len(m[ingredient]) == 1:
      to_remove |= m[ingredient]

  for ingredient in m:
    if len(m[ingredient]) != 1:
      m[ingredient] -= to_remove


print(','.join([list(m[k])[0] for k in sorted(m.keys())]))
