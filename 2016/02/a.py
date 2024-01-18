keypad = ['123','456','789']
r,c = 1,1
lines = open('input.txt').read().strip().split('\n')
for line in lines:
  for op in line:
    if op == 'L':
      c = max(0,c - 1)
    if op == 'R':
      c = min(2,c + 1)
    if op == 'U':
      r = max(0,r - 1)
    if op == 'D':
      r = min(2,r + 1)
  print(keypad[r][c],end='')
print()
