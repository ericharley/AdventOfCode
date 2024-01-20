import itertools
lines = open('input.txt').read().strip().split('\n')
t = 0
for line in lines:
  xs = list(map(int, line.split()))
  for a,b in itertools.combinations(xs, 2):
    if a % b == 0:
       t += a//b
       break
    elif b % a == 0:
       t += b//a
       break
print(t)


