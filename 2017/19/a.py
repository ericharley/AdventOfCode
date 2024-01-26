data = open('input.txt').read()

l = {ch for ch in data if ch not in ' +-|\n'}
r, c = 0, data.index('|')
dir = 'S'
steps = 0
path = ''

data = data.splitlines()

while l:
  ch = data[r][c]

  if ch in l:
    path += ch
    l.remove(ch)

  elif ch == '+':
    if dir in 'NS':
      dir = 'W' if data[r][c-1] != ' ' else 'E'
    elif dir in 'EW':
      dir = 'N' if data[r-1][c] != ' ' else 'S'

  r,c = {'S':(r+1,c), 'N':(r-1,c), 'W':(r,c-1), 'E':(r,c+1)}[dir]
  steps += 1

# Part 1
print(path)

# Part 2
print(steps)
