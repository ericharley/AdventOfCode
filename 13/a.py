import numpy as np

paper = np.zeros((892+1, 1310+1), dtype=int)

with open("input.txt", "r") as file:
  lines = file.readlines()

ins = []
for line in lines:
 line = line.rstrip('\n')
 if line == '':
   continue
 if line.startswith('fold'):
   (_,_,d) = line.split(' ')
   (d,v) = d.split('=')
   v = int(v)
   ins.append([d,v])
 else:
   (x,y) = line.split(',')
   x = int(x)
   y = int(y)
   paper[y,x] = 1

part1 = True
for op in ins:
   (d,v) = op
   if d == 'y':
     top = paper[0:v,:]
     bottom = np.flipud(paper[v+1:,:])
     if (np.shape(top)[0] < np.shape(bottom)[0]):
       top    = np.pad(top, pad_width=((np.shape(bottom)[0] - np.shape(top)[0], 0),(0,0)))
     else:
       bottom = np.pad(bottom, pad_width=((np.shape(top)[0] - np.shape(bottom)[0], 0),(0,0)))
     res = top + bottom
     paper = res
   elif d =='x':
     top = paper[:,0:v]
     bottom = np.fliplr(paper[:,v+1:])
     res = top + bottom
     paper = res

   if part1:
     paper[paper > 1] = 1
     print((np.sum(paper)))
     part1 = False

for r in range(6):
 for c in range(40):
  if int(paper[r,c]) >= 1:
    print('#', end='')
  else:
    print('.', end='')
 print('')
