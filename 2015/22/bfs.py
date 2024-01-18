POISSON_DURATION = 6
SHIELD_DURATION = 6
RECHARGE_DURATION = 5
	
HP_START = 50
MANA_START = 500
	
BOSS_HP_START = 55
BOSS_DAMAGE = 8

def cost(state):
  (HP, MANA, BOSS_HP, SHIELD_LEFT, POISON_LEFT, RECHARGE_LEFT, PLAYER_TURN, COST) = state
  return COST

def is_win(state):
  (HP, MANA, BOSS_HP, SHIELD_LEFT, POISON_LEFT, RECHARGE_LEFT, PLAYER_TURN, COST) = state
  return (HP > 0 and BOSS_HP <= 0)

def addHard(s):
  (HP, MANA, BOSS_HP, SHIELD_LEFT, POISON_LEFT, RECHARGE_LEFT, PLAYER_TURN, COST) = s
  if PLAYER_TURN:
    HP -= 1
  return (HP, MANA, BOSS_HP, SHIELD_LEFT, POISON_LEFT, RECHARGE_LEFT, PLAYER_TURN, COST)

def neighbors(state):
   (HP, MANA, BOSS_HP, IN_SHIELD_LEFT, IN_POISON_LEFT, IN_RECHARGE_LEFT, PLAYER_TURN, COST) = state

   ARMOR_EFFECT    = 7   if IN_SHIELD_LEFT   > 0 else 0
   POISON_EFFECT   = 3   if IN_POISON_LEFT   > 0 else 0
   RECHARGE_EFFECT = 101 if IN_RECHARGE_LEFT > 0 else 0

   SHIELD_LEFT = max(0,IN_SHIELD_LEFT-1)
   POISON_LEFT = max(0,IN_POISON_LEFT-1)
   RECHARGE_LEFT = max(0,IN_RECHARGE_LEFT-1)

   n = []

   EFFECTIVE_BOSS_DAMAGE = max(1,BOSS_DAMAGE-ARMOR_EFFECT)
   BOSS_HP -= POISON_EFFECT
   MANA += RECHARGE_EFFECT

   if PLAYER_TURN:

     #if cast Magic Missile:
     if MANA >= 53:
       n.append((HP, MANA-53, BOSS_HP-4, SHIELD_LEFT, POISON_LEFT, RECHARGE_LEFT, not PLAYER_TURN, COST+53))

     #if cast Drain:
     if MANA >= 73:
       n.append((HP+2, MANA-73, BOSS_HP-2, SHIELD_LEFT, POISON_LEFT, RECHARGE_LEFT, not PLAYER_TURN, COST+73))

     #if cast Shield:
     if MANA >= 113:
       if SHIELD_LEFT == 0:
         n.append((HP, MANA-113, BOSS_HP, SHIELD_DURATION, POISON_LEFT, RECHARGE_LEFT, not PLAYER_TURN, COST+113))

     #if cast Poison:
     if MANA >= 173:
       if POISON_LEFT == 0:
         n.append((HP, MANA-173, BOSS_HP, SHIELD_LEFT, POISSON_DURATION, RECHARGE_LEFT, not PLAYER_TURN, COST+173))

     #if cast Recharge:
     if MANA >= 229:
       if RECHARGE_LEFT == 0:
         n.append((HP, MANA-229, BOSS_HP, SHIELD_LEFT, POISON_LEFT, RECHARGE_DURATION, not PLAYER_TURN, COST+229))

   else: #BOSS_TURN:
     n.append((HP-EFFECTIVE_BOSS_DAMAGE, MANA, BOSS_HP, SHIELD_LEFT, POISON_LEFT, RECHARGE_LEFT, not PLAYER_TURN, COST))

   return n
   
def do_run(HARD_MODE):
    min_cost = 10000
    q = []
    visited = {}

    start = (HP_START, MANA_START, BOSS_HP_START, 0, 0, 0, True, 0)
    if HARD_MODE:
      start = addHard(start)
    
    visited[start] = True
    q.append(start)

    while q:

      current_state = q.pop()

      if is_win(current_state):
        min_cost = min(min_cost, cost(current_state))

      for nxt in neighbors(current_state):
        if HARD_MODE:
          nxt = addHard(nxt)
        if nxt not in visited and cost(nxt) < min_cost:
          visited[nxt] = True
          q.append(nxt)

    return min_cost

# Part 1
print(do_run(HARD_MODE=False))

# Part 2
print(do_run(HARD_MODE=True))
