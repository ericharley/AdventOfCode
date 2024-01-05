from collections import deque

#cups = deque(map(int,'389125467'))
cups = deque(map(int,'135468729'))

N = len(cups)

def domove(cups):

# current cup is cup at location 0
# rotate the list so that the current cup is always at the first position (idx 0?

# the crab picks up three cups that are immediately clockwise of the current cup
# remove them from the circle
# s = cups[1:4]
  cups.rotate(-1)
  s = [cups.popleft(),cups.popleft(),cups.popleft()]
  cups.rotate(1)

# ( destination cup logic )
# The crab selects a destination cup with a label equal to the current cup's label
#  minus one, if this would select one of the cups we just picked up
# then we go down one at a time to the next cup
  dest_cup = cups[0] - 1
  if dest_cup == 0:
    dest_cup += N
  while dest_cup in s:
    dest_cup = (dest_cup - 1) % N
    if dest_cup == 0:
      dest_cup += N

  dest_idx = cups.index(dest_cup)

  cups.rotate(-dest_idx)
#  cups = cups[0:1] + s + cups[1:]
  cups.insert(1,s.pop())
  cups.insert(1,s.pop())
  cups.insert(1,s.pop())
  cups.rotate(dest_idx)
  return cups

N_moves = 100
for i in range(N_moves):
  cups = domove(cups)
  cups.rotate(-1)

r = cups.index(1)
cups.rotate(-r)
cups.popleft()
s = ''.join(map(str, cups))
print(s)
