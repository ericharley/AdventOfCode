row = open('input.txt').read().strip()

def f(row):
  row = '.' + row + '.'
  return ''.join(['^' if row[i-1] != row[i+1] else '.' for i in range(1,len(row)-1)])

t = 0
for i in range(40):
  t += row.count('.')
  row = f(row)
print(t)

t = 0
for i in range(400000):
  t += row.count('.')
  row = f(row)
print(t)

