from fractions import Fraction
import itertools

class Point:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

lines = open('input.txt').read().strip().split('\n')
#lines = open('test.txt').read().strip().split('\n')

x_min = 7
x_max = 27
x_min = 200000000000000
x_max = 400000000000000

y_min = x_min
y_max = x_max

points = set()

for line in lines:
 (px,py,pz,vx,vy,vz) = map(int,line.replace('@',',').replace(' ','').split(','))
 points.add(Point(px,py,pz,vx,vy,vz))

count = 0
for p, q in itertools.combinations(points, 2):

    if (p.vx*q.vy - p.vy*q.vx) == 0 :
      continue

    lambda_p = Fraction( ( p.y*q.vx - p.x*q.vy + q.vy*q.x - q.vx*q.y),(p.vx*q.vy - p.vy*q.vx))
    lambda_q = Fraction( (-p.vy*p.x + p.vx*p.y + p.vy*q.x - p.vx*q.y),(p.vx*q.vy - p.vy*q.vx))

    r = (p.x + lambda_p*p.vx, p.y + lambda_p*p.vy)

    if lambda_p <= 0 or lambda_q <= 0:
      continue

    if x_min <= r[0] <= x_max and y_min <= r[1] <= y_max:
        count += 1

print(count)
