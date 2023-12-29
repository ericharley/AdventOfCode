class Point:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def __repr__(self):
        return f'{(self.x, self.y, self.z, self.vx, self.vy, self.vz)}'

lines = open('input.txt').read().strip().split('\n')
#lines = open('test.txt').read().strip().split('\n')
#lines = open('test2.txt').read().strip().split('\n')


points = []

from collections import defaultdict

vs = defaultdict(list)

for line in lines:
 (px,py,pz,vx,vy,vz) = map(int,line.replace('@',',').replace(' ','').split(','))
 vs[vx] += [Point(px,py,pz,vx,vy,vz)]
 points.append(Point(px,py,pz,vx,vy,vz))


a = points[0]
b = points[1]
c = points[2]

print('{x+y+z}/.Solve[{',end='')
i = 0
for p in [a,b,c]:
 i += 1
 print(f'x + t{i}*vx == {p.x} + t{i}*{p.vx},',end='\n')
 print(f'y + t{i}*vy == {p.y} + t{i}*{p.vy},',end='\n')
 print(f'z + t{i}*vz == {p.z} + t{i}*{p.vz}',end='\n')
 if i != 3:
   print(',',end='')
print('}]')

for key in vs:
 if len(vs[key]) == 3:
   print(vs[key])
