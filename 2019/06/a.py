f = open("input.txt")
lines = f.readlines()

r = {}

for line in lines:
 a,b = line.rstrip().split(')')
 r[b] = a

def n(obj):
  if obj == 'COM':
    return 0
  return n(r[obj]) + 1  

print( sum([n(obj) for obj in r]) )
