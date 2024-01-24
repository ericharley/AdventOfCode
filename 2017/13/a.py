lines = open('input.txt').read().strip().split('\n')

depth = {}

for line in lines:
  layer,_depth = map(int,line.split(': '))
  depth[layer] = _depth

def caught(t,n):
  return (t % (2*(n-1))) == 0

# Part 1
score = sum([layer*depth[layer] for layer in depth if caught(layer, depth[layer])])
print(score)


# Part 2
for delay in range(10**7):
  for layer in depth:
    if caught(layer+delay, depth[layer]):
      break
  else:
    break

print(delay)

