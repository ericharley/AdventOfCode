lines = open('input.txt').read().strip().split('\n')
t = 0
for line in lines:
  line = line.split()
  if len(line) == len(set(line)):
    t += 1

print(t)

t = 0
for line in lines:
  line = line.split()
  line = [''.join(sorted(x)) for x in line]
  if len(line) == len(set(line)):
    t += 1
print(t)
