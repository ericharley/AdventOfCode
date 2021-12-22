# number of wins for each player start from this state
def u2(p1, s1, p2, s2):
  p1_wins = 0
  p2_wins = 0
  
  # player 1 rolls
  # for each possible roll of the quantum dice 3 times
  for r in [x+y+z for x in [1,2,3] for y in [1,2,3] for z in [1,2,3]]:
    # player 2 rolls
    for r2 in [x+y+z for x in [1,2,3] for y in [1,2,3] for z in [1,2,3]]:   
      p1_ = (p1 + r - 1) % 10 + 1
      s1_ = s1 + p1_

      p2_ = (p2 + r2 - 1) % 10 + 1
      s2_ = s2 + p2_

      # if player one wins on this roll, then stop player 2
      if s1_ >= 21:
        p1_wins += 1
        break

      # if player one doesn't win, then keep going with player 2
      elif s2_ >= 21:
         p2_wins += 1
         continue

      # neither player won on this roll, 
      else:
        dx, dy = u2(p1_, s1_, p2_, s2_)
        p1_wins += dx
        p2_wins += dy
      
  return p1_wins,p2_wins

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        #Warning: You may wish to do a deepcopy here if returning objects
        return self.memo[args]

u2 = Memoize(u2)

with open("input.txt","r") as file:
#with open("test.txt","r") as file:
  p1_0 = int(file.readline().rstrip('\n')[-1])
  p2_0 = int(file.readline().rstrip('\n')[-1])
  print(max(u2(p1_0,0,p2_0,0)))
