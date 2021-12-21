def u(p1, p2, s1=0, s2=0):
  # compute win counts starting from this state, player 1 to roll
  p1_wins = 0
  p2_wins = 0

  # for each possible roll of the quantum dice 3 times
  for r in [x+y+z for x in [1,2,3] for y in [1,2,3] for z in [1,2,3]]:
   # update the posistion and score of player 0
   p1_ = (p1 + r - 1) % 10 + 1
   s1_ = s1 + p1_

   # if player 0 wins on this roll, then record the win.
   if s1_ >= 21:
     p1_wins += 1
 
   # otherwise, recurse by swapping roll of player 1 and 2, using new positions
   # return number of times each player one, unswapping
   else:
     extra_p2_wins, extra_p1_wins = u(p2, p1_, s2, s1_)
     p1_wins += extra_p1_wins
     p2_wins += extra_p2_wins

  return [p1_wins,p2_wins]

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        #Warning: You may wish to do a deepcopy here if returning objects
        return self.memo[args]

u = Memoize(u)

with open("input.txt","r") as file:
#with open("test.txt","r") as file:
  p1_0 = int(file.readline().rstrip('\n')[-1])
  p2_0 = int(file.readline().rstrip('\n')[-1])
  print(max(u(p1_0,p2_0)))
