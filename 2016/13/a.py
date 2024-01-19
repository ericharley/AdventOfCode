from collections import defaultdict

id = 1350
gx,gy = 31,39

def t(x,y):
  if bin((x*x + 3*x + 2*x*y + y + y*y) + id)[2:].count('1') % 2 == 0:
    return '.'
  else:
    return '#'

visited = {}
q = []
dist = defaultdict(int)

start = (1,1)

q.append(start)
dist[start] = 0

while q:
  x,y = q.pop(0)
  if (gx,gy) == (x,y):
    print(dist[x,y])
    break
  else:
    for (nx,ny) in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
      if nx >= 0 and ny >= 0 and t(nx,ny) == '.' and (nx,ny) not in visited:
        visited[nx,ny] = True
        dist[nx,ny] = dist[x,y] + 1
        q.append((nx,ny))

print(len([x for x in dist if dist[x] <= 50]))
