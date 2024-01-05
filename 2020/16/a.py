lines = open('input.txt').read().strip()

# Parse input
rules, ticket, nearby = lines.split('\n\n')

rules = rules.split('\n')
def doit(s):
  label, values = s.split(': ')
  values = values.split(' or ')
  values = list(map(lambda x : list(map(int,x.split('-'))), values))
  return [label,values]

rules = list(map(doit, rules))
r = {}
for label, values in rules:
  r[label] = values

ticket = list(map(int,ticket.split('\n')[1].split(',')))
# how many fields are there?
N = len(ticket)

nearby = nearby.split('\n')[1:]
nearby = list(map(lambda x : list(map(int,x.split(','))), nearby))

# Part 1
total = 0
valid = []

for t in nearby:
  for v in t:
    for label,values in rules:
      if any([m <= v <= M for m, M in values]):
        break
    else:
      # ticket t is invalid at value v
      total += v
      break
  else:
    # ticket is valid
    valid.append(t)

print(total)


# Part 2

f = {}
for field in range(N):
  f[field] = set(r.keys())

# for each valid ticket
for t in valid:
  # for each field in the ticket
  for field, value in enumerate(t):
    # for each label, see if it could be valid for the field
    to_remove = set()
    for label in f[field]:
      # if the value of the field in this ticket doesn't fit,
      #    then remove it from consideration
      if not any([m <= value <= M for m, M in r[label]]):
        to_remove.add(label)
    f[field] -= to_remove

while True:
  to_remove = set()

  for field in f:
    if len(f[field]) == 1:
      to_remove |= f[field]

  for field in f:
    if len(f[field]) != 1:
      f[field] -= to_remove

  if all([len(f[field]) == 1 for field in f]):
    break

t = 1
for v in [ticket[field_number] for field_number, v in f.items() if 'departure' in list(v)[0]]:
  t *= v
print(t)
