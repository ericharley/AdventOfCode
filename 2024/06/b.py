grid = open('input.txt').read().splitlines()

def g(r,c):
  return c - r*1j

board = { g(r,c) : grid[r][c] for r,row in enumerate(grid) for c,col in enumerate(row) }
starting_pos = [z for z,h in board.items() if h not in '.#' ][0]
starting_heading = +1j
m = { b for b in board if board[b] == '#' }

def do_move(pos,heading):
  _pos, _heading = pos + heading, heading
  if _pos in m:
    _pos, _heading = pos, heading * -1j
  return _pos, _heading

# Part 1
pos,heading = starting_pos, starting_heading
path = set()
while pos in board:
  path.add(pos)
  pos,heading = do_move(pos,heading)

print(len(path))


# Part 2
t = 0
for new_obs in path:
    m.add(new_obs)

    pos,heading = starting_pos, starting_heading
    visited = set()

    while pos in board and (pos,heading) not in visited:
      visited.add((pos,heading))
      pos, heading = do_move(pos, heading)

    if (pos,heading) in visited:
      t += 1

    m.remove(new_obs)

print(t)
