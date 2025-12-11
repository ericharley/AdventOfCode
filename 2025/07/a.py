g = open('input.txt').read().strip().split()

from functools import lru_cache

@lru_cache
def f(r,c):

  if (r < 0) or (r >= len(g)) or (c < 0) or (c >= len(g[0])):
    return 0
  if g[r][c] == 'S':
    return 1
  if g[r-1][c] == '^':
    return 0
  if g[r][c] != '^' and f(r-1,c) == 1 :
    return 1
  if c!= len(g[0])-1 and f(r-1,c) == 0 and g[r][c+1] == '^' :
    return f(r-1,c+1)
  if c!= 0 and f(r-1,c) == 0 and g[r][c-1] == '^' :
    return f(r-1,c-1)

  return 0

for r in range(len(g)):
 for c in range(len(g[0])):
  v = f(r,c)
  if v == 0 or g[r][c] == 'S':
    ch = g[r][c]
  elif v == 1:
    ch = '|'
  print( ch,end='' )

 print()

#r = len(g) - 1
#print( sum([f(r,c) for c in range(len(g[0]))]) )

t = 0
for r in range(len(g)):
 for c in range(len(g[0])):
  if g[r][c] == '^' and f(r-1,c):
    t += 1

print(t)

@lru_cache
def h(r,c):
  t = 0
  if (r < 0) or (r >= len(g)) or (c < 0) or (c >= len(g[0])):
    return 0
  if g[r][c] == 'S':
    return 1
  if f(r,c) == 1:
    t += h(r-1,c)
  if c!= 0 and g[r][c-1] == '^' :
    t += h(r-1,c-1)
  if c!= len(g[0])-1 and g[r][c+1] == '^' :
    t += h(r-1,c+1)
  return t
  
r = len(g) - 1
print( sum([h(r,c) for c in range(len(g[0]))]) )
