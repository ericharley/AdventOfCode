from collections import deque

p_l = 25

lines = list(map(int,open('input.txt').read().strip().split('\n')))
code = deque(maxlen=p_l)

for i,n in enumerate(lines):
  if i < p_l or any([n-c in code for c in code if n-c!=c]):
    code.append(n)
  else:
    break

# Part 1
print(n)

# Part 2
def prefix_sums(A):
  n = len(A)
  P = [0] * (n + 1)
  for k in range(1, n + 1):
      P[k] = P[k - 1] + A[k - 1]
  return P

def count_total(P, x, y):
    return P[y + 1] - P[x]

P = prefix_sums(lines)

for x in range(len(lines)):
  for y in range(x+1,len(lines)):
    if count_total(P, x, y) == n:
      vals = [lines[n] for n in range(x,y+1)]
      print( min(vals) + max(vals) )
