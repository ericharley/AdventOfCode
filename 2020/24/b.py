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
  for d in lineToList(line):
    dq,dr = v[d]
    q += dq
    r += dr
  board[q,r] = 1 - board[q,r]

def neighbors(q,r):
  for dq,dr in v.values():
    yield q+dq,r+dr

# Part 1
print(sum(board.values()))

# Part 2
N = 100
for i in range(N):

  newBoard = defaultdict(int)

  c = defaultdict(int)
  for q,r in board:
    if board[q,r] == 1:
      for nq,nr in neighbors(q,r):
        c[nq,nr] += 1

  for q,r in (set(board) | set(c)):
    if board[q,r] == 0 and c[q,r] == 2:
        newBoard[q,r] = 1
    elif board[q,r] == 1:
      if not (c[q,r] == 0 or c[q,r] > 2):
        newBoard[q,r] = 1

  board = newBoard

print(sum(board.values()))
