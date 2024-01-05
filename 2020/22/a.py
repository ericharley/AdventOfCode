p1, p2 = open('input.txt').read().strip().split('\n\n')

p1 = list(map(int, p1.split('\n')[1:]))
p2 = list(map(int, p2.split('\n')[1:]))

while p1 and p2:
  a = p1.pop(0)
  b = p2.pop(0)

  if a < b :
    p2.append(b)
    p2.append(a)

  else:
    p1.append(a)
    p1.append(b)

p = p1 + p2
n = len(p)
print(sum([(n-i)*v for i,v in enumerate(p)]))
