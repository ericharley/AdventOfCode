import math

filename = 'input.txt'
lines = open(filename).readlines()
times = list(map(int, lines[0].split()[1:]))
dists = list(map(int, lines[1].split()[1:]))


#Part 1
# count a time t if t*(T-t) - D > 0
p = 1
for T, D in list(zip(times,dists)):
  v = sum([1 if t*(T-t)>D else 0 for t in range(T)])
  p *= v
print(p)


#Part 2
times = [int(''.join(list(lines[0].split()[1:])))]
dists = [int(''.join(list(lines[1].split()[1:])))]

## Slow
#p = 1
#for T, d in list(zip(times,dists)):
#  v = sum([1 if t*(T-t)>d else 0 for t in range(T)])
#  p *= v
#print(p)
#
# or
#
# Fast
# solving for t, we have
# T/2 - 1/2*math.sqrt(-4*D + T**2) < t < T/2 + 1/2*math.sqrt(-4*D + T**2)
T = times[0]
D = dists[0]
U = math.floor(T/2 + 1/2*math.sqrt(-4*D + T**2))
L =  math.ceil(T/2 - 1/2*math.sqrt(-4*D + T**2))
v = U - L + 1

print(v)
