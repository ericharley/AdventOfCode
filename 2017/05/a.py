filename = 'input.txt'
jmps = list(map(int,open(filename).read().strip().split('\n')))

i,c = 0,0

while 0 <= i < len(jmps):
  jmp = jmps[i]
  jmps[i] += 1
  i += jmp
  c += 1
 
print(c)


jmps = list(map(int,open(filename).read().strip().split('\n')))
i,c = 0,0

while 0 <= i < len(jmps):
  jmp = jmps[i]
  if jmps[i] >= 3:
    jmps[i] -= 1
  else:
    jmps[i] += 1
  i += jmp
  c += 1
 
print(c)

