cur = {}
counts = [0,0]

# Input:
# Player 1 starting position: 7
# Player 2 starting position: 9

cur[(7,0,9,0)] = 1

while len(cur) > 0:
 nxt = {}
 # for each possible state
 for (p0,s0,p1,s1) in cur :

  # for each possible roll by player 0
  for roll0 in [x+y+z for x in [1,2,3] for y in [1,2,3] for z in [1,2,3]]:
    # update the posistion and score of player 0
    p0_ = (p0 + roll0 - 1) % 10 + 1
    s0_ = s0 + p0_

    # if player 0 wins from this state on this roll, then map these states into wins
    if s0_ >= 21:
      counts[0] += cur[(p0,s0,p1,s1)]
      continue
 
    # if player 0 does not win from this state on this roll, then player 1 rolls
    for roll1 in [x+y+z for x in [1,2,3] for y in [1,2,3] for z in [1,2,3]]:
      # update the posistion and score of player 1
      p1_ = (p1 + roll1 - 1) % 10 + 1
      s1_ = s1 + p1_
 
      # if player 1 wins from this state on this roll, then map these states into wins      
      if s1_ >= 21:
        counts[1] += cur[(p0,s0,p1,s1)]
  
      # otherwise, neither player wins from this state on these rolls, so we propagate
      # the state counts
      else:
        nxt[(p0_,s0_,p1_,s1_)] = nxt.get((p0_,s0_,p1_,s1_),0) + cur[(p0,s0,p1,s1)]

 cur = nxt

print(max(counts))
