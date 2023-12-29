filename = 'test.txt'
filename = 'input.txt'
lines = list(map(lambda x : x.split(), open(filename).readlines()))

x = 0
y = 0

coords = []
coords.append((x,y))
path_len = 1
for line in lines:
  dir, N, color = line
  N = int(N)
  color = color[2:-1],16
  #print(dir,N,color)

#  dx = 0
#  dy = 0
#  if dir == 'U':
#     dy = -1
#
#  if dir == 'D':
#     dy = +1
#
#  if dir == 'L':
#     dx = -1
#
#  if dir == 'R':
#     dx = +1
#
#  for _ in range(N):
#    x += dx
#    y += dy
#    coords.append((x,y))

  dx = 0
  dy = 0
  if dir == 'U':
     dy = -N

  if dir == 'D':
     dy = +N

  if dir == 'L':
     dx = -N

  if dir == 'R':
     dx = +N

  x += dx
  y += dy
  coords.append((x,y))
  path_len += N

#coords.pop()
#print(coords)

def polygonArea(vertices):
  N = len(vertices)
  sum = 0
  for i in range(0, N):
    sum += vertices[i][0] *  vertices[(i+1) % N][1]
    sum -= vertices[i][1] *  vertices[(i+1) % N][0]
  area = abs(sum) // 2
  return area

# by Pick's theorem,
# A = i + b/2 - 1
# so the area we want is really the number of integer points
#
# i + b = A + b/2 + 1

point_area = polygonArea(coords) + path_len//2 + 1

#print(len(coords), path_len)
  
#print(polygonArea(points) - len(loop)//2 +1)
print(point_area)
