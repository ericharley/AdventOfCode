from collections import defaultdict
m = defaultdict(int)
claims = set()

lines = open('input.txt').read().strip().split('\n')
for line in lines:
  (id,_,x,y,l,w) = line.replace('#','').replace(':','').replace('x',' ').replace(',',' ').split()
  claims.add((id,int(x),int(y),int(l),int(w)))

for id,x,y,l,w in claims:
  for i in range(l):
    for j in range(w):
      m[(x+i,y+j)] += 1

# Part 1
print(sum([1 for x in m if m[x] >= 2]))

# Part 2
for id,x,y,l,w in claims:
  if all( [m[x+i,y+j] == 1 for i in range(l) for j in range(w)]):
    print(id)
    break
