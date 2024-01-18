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
    b = b.replace(',','')

    if r[a] != int(b):
      break

  else:
    print(id)
