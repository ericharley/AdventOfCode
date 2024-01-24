lines = open('input.txt').read().strip().split('\n')

def find(data, i):
    if i != data[i]:
        data[i] = find(data, data[i])
    return data[i]

def union(data, i, j):
    pi, pj = find(data, i), find(data, j)

    if pi != pj:
        data[pi] = pj

data = [i for i in range(2000)]

for line in lines:
  frm,right = line.split(' <-> ')
  frm = int(frm)
  for to in list(map(int,right.split(', '))):
    union(data, frm, to)

# Part 1
print(sum([find(data, i) == find(data, 0) for i in range(2000)]))

# Part 2
ccs = set()
for i in range(2000):
  ccs.add(find(data,i))

print(len(ccs))
