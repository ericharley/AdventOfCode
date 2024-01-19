import intervals as I

lines = open('input.txt').read().strip().split('\n')

fw = I.empty()
for line in lines:
 a,b = map(int,line.split('-'))
 fw = fw | I.closed(a,b)

N = 2**32 - 1
space = I.closed(0,N) - fw

t = 0
min_L = N
for a in space:

  L = a.lower + (not a.left)
  U = a.upper - (not a.right)

  if L <= U:
    min_L = min(min_L,L)
    t += (U - L + 1)

# Part 1
print(min_L)

# Part 2
print(t)
