from collections import defaultdict
from collections import deque

def f(num_players, num_moves):
  scores = defaultdict(int)

  d = deque([0])

  for i in range(1,num_moves+1):
    if i % 23 == 0:
      d.rotate(7)
      scores[i%num_players] += i + d.popleft()
    else:
      d.rotate(-2)
      d.appendleft(i)

    #k = d.index(0)
    #d.rotate(-k)
    #print(i%num_players, d)
    #d.rotate(k)

  return max(scores.values())

# 427 players; last marble is worth 70723 points
num_players = 427
num_moves = 70723

# Part 1
print(f(num_players, num_moves))

# Part 2
num_moves *= 100
print(f(num_players, num_moves))

