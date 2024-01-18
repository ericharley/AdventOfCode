r = {
 'children': 3,
 'cats': 7,
 'samoyeds': 2,
 'pomeranians': 3,
 'akitas': 0,
 'vizslas': 0,
 'goldfish': 5,
 'trees': 3,
 'cars': 2,
 'perfumes': 1
}

lines = open('input.txt').read().strip().split('\n')

for line in lines:
  id = line.split()[1].replace(':','')

  fields = line.split()
  fields.pop(0)
  fields.pop(0)

  for a,b in zip(fields[0::2], fields[1::2]):
    a = a.replace(':','')
    b = int(b.replace(',',''))

    if a in ['cats','trees'] and b <= r[a]:
      break

    if a in ['pomeranians','goldfish'] and b >= r[a]:
      break

    if a not in ['cats','trees','pomeranians','goldfish'] and r[a] != b:
      break

  else:
    print(id)
