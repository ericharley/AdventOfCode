import re
import numpy as np

ins = {}
a = {}
with open("input.txt","r") as file:
#with open("test.txt","r") as file:
#with open("test2.txt","r") as file:
  for line in file.readlines():
     line = line.rstrip('\n')
     if line[0:2] == 'on':
       op = 1
     else:
       op = 0
     pattern = r'\-?[0-9]+'
     x = re.findall(pattern, line)
     l = list(map(int, x))
     x0 = l[0]
     x1 = l[1]
     y0 = l[2]
     y1 = l[3]
     z0 = l[4]
     z1 = l[5]
     ins[(op,x0,x1,y0,y1,z0,z1)] = 1
#     print(line)
#     print(x0,x1,y0,y1,z0,z1)

for (op,x0,x1,y0,y1,z0,z1) in ins:

  l = max(x0, -50)
  u = min(x1, 50)
  if l > u or u < l:
   o = []
   continue
  else:
   o = [l,u]
  #print(l,u)
  (x0,x1) = o

  l = max(y0, -50)
  u = min(y1, 50)
  if l > u or u < l:
   o = []
   continue
  else:
   o = [l,u]
  (y0,y1) = o

  l = max(z0, -50)
  u = min(z1, 50)
  if l > u or u < l:
   o = []
   continue
  else:
   o = [l,u]
  (z0,z1) = o

  if op == 1:
    for x in range(x0,x1+1):
      for y in range(y0,y1+1):
        for z in range(z0,z1+1):
          a[(x,y,z)] = 1
  else:
    for x in range(x0,x1+1):
      for y in range(y0,y1+1):
        for z in range(z0,z1+1):
          if (x,y,z) in a:
           del a[(x,y,z)]
  
print(len(a))
