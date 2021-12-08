with open("input.txt", "r") as f:
# with open("test.txt", "r") as f:
   lines = f.readlines()

c = 0

for line in lines:
   line = line.rstrip('\n')
   g = line.split(' | ')
   v = g[1].split(' ')
   s = [len(x) for x in v]
   r = list(filter(lambda x : x in [2,3,4,7], s))
   c += len(r)

print(c)
