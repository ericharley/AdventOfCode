from collections import defaultdict

lines = open('input.txt').read().strip().split('\n')

board = defaultdict(int)

def lineToList(line):
  output = []
  last_ch = ''
  for ch in line:
    if ch == 'e' or ch == 'w':
      output.append(last_ch+ch)
      last_ch = ''
    else:
      last_ch = ch
  return output

v = {
 'e'  : (+1,0),
 'w'  : (-1,0),
 'ne' : (+1,-1),
 'nw' : (0,-1),
 'se' : (0,+1),
 'sw' : (-1,+1),
}

for line in lines:
  q,r = 0,0
  dirs = lineToList(line)
  for d in dirs:
    dq,dr = v[d]
    q += dq
    r += dr
  board[q,r] = 1 - board[q,r]

print(sum(board.values()))
