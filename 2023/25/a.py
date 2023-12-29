lines = open('input.txt').read().strip().split('\n')

def find(data, i):
    if i != data[i]:
        data[i] = find(data, data[i])
    return data[i]

def union(data, i, j):
    pi, pj = find(data, i), find(data, j)

    if pi != pj:
        data[pi] = pj

vertices = {}
edges = {}

for line in lines:
  left, right = line.split(': ')
  right = right.split(' ')

  vertices[left] = left
  for v in right:
    vertices[v] = v
    edges[(v,left)] = 1

#kzx -- qmr
#nvb -- fts
#zns -- jff

del edges[('qmr','kzx')]
del edges[('fts','nvb')]
del edges[('jff','zns')]

# union
for i,j in edges:
  union(vertices, i, j)

count = {find(vertices, v) : 0 for v in vertices}
red = list(count)[0]
green = list(count)[1]
for v in vertices:
   count[find(vertices, v)] += 1

#print(red,green)

#for v in vertices:
#  if find(vertices,v) == red:
#    print(f'{v} [color="red", style=filled]')
#
#  if find(vertices,v) == green:
#    print(f'{v} [color="green", style=filled]')

p = 1
for c in count:
 p *= count[c] 
print(p)

