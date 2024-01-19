lines = open('input.txt').read().strip().split('\n')
fw = []
for line in lines:
 a,b = line.split('-')
 a = int(a)
 b = int(b)
 fw.append((a,b))

for i in range(2**32):
  for a,b in fw:
    if a <= i <= b:
      break
  else:
    print(i)
    break
