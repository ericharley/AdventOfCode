vertices = set()
m = {}

lines = open('input.txt').read().strip().split('\n')
for line in lines:
  f = line.split()
  node = f[0]
  node = node.replace('/dev/grid/node-','')
  (x,y) = node.split('-')  
  x = int(x.replace('x',''))
  y = int(y.replace('y',''))
  size = int(f[1].replace('T',''))
  used = int(f[2].replace('T',''))
  avail = int(f[3].replace('T',''))

  vertices.add((x,y))

  m[x,y] = (size,used,avail)

for y in range(0,28):
  for x in range(0,37):
    c = '.'
    if m[x,y][0] > 100:
      c = '='
    if m[x,y][1] == 0:
      c = '_'
    if (x,y) == (36,0):
      c = 'G'
    print(c,end=' ')
  print()

#
#t = 0
#for x,y in m:
# for xp,yp in m:
#   xp_size,xp_used,xp_avail = m[xp,yp]
#   x_size,x_used,x_avail = m[x,y]
#   if (x,y) != (xp,yp):
#     if x_used > 0:
#       if x_used <= xp_avail:
#         t += 1
#
#print(t)
      

