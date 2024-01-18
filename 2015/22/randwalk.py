import random

def is_valid(state):
  (HP, MANA, BOSS_HP, SHIELD_LEFT, POISON_LEFT, RECHARGE_LEFT, PLAYER_TURN, COST) = state

  if HP < 0 or MANA < 0:
    return False
  return True

def is_done(state):
  (HP, MANA, BOSS_HP, SHIELD_LEFT, POISON_LEFT, RECHARGE_LEFT, PLAYER_TURN, COST) = state

  if HP > 0 and BOSS_HP == 0:
    return True
  return False
	
def is_win(state):
  (HP, MANA, BOSS_HP, SHIELD_LEFT, POISON_LEFT, RECHARGE_LEFT, PLAYER_TURN, COST) = state

  if HP > 0 and BOSS_HP == 0:
    return True
  return False

def bad_cost(state, min_cost):
  (HP, MANA, BOSS_HP, SHIELD_LEFT, POISON_LEFT, RECHARGE_LEFT, PLAYER_TURN, COST) = state

  return COST > min_cost

def neighbors(state, BOSS_DAMAGE, HARD_MODE):
   (HP, MANA, BOSS_HP, SHIELD_LEFT, POISON_LEFT, RECHARGE_LEFT, PLAYER_TURN, COST) = state

   POISSON_DURATION = 6
   SHIELD_DURATION = 6
   RECHARGE_DURATION = 5
	
   ARMOR_EFFECT    = 7   if SHIELD_LEFT   > 0 else 0
   POISON_EFFECT   = 3   if POISON_LEFT   > 0 else 0
   RECHARGE_EFFECT = 101 if RECHARGE_LEFT > 0 else 0

   BOSS_TURN = not PLAYER_TURN

   n = []

   if PLAYER_TURN:
     #if cast Magic Missile:
     n.append((max(0,HP-HARD_MODE), MANA-53+RECHARGE_EFFECT, max(0,BOSS_HP-4-POISON_EFFECT), max(0,SHIELD_LEFT-1), max(0,POISON_LEFT-1), max(0,RECHARGE_LEFT-1), not PLAYER_TURN, COST+53))

     #if cast Drain:
     if HP-HARD_MODE > 0:
       n.append((max(0,HP-HARD_MODE+2), MANA-73+RECHARGE_EFFECT, max(0,BOSS_HP-2-POISON_EFFECT), max(0,SHIELD_LEFT-1), max(0,POISON_LEFT-1), max(0,RECHARGE_LEFT-1), not PLAYER_TURN, COST+73))

     #if cast Shield:
     if SHIELD_LEFT <= 1:
       n.append((max(0,HP-HARD_MODE), MANA-113+RECHARGE_EFFECT, max(0,BOSS_HP-POISON_EFFECT), SHIELD_DURATION, max(0,POISON_LEFT-1), max(0,RECHARGE_LEFT-1), not PLAYER_TURN, COST+113))

     #if cast Poison:
     if POISON_LEFT <= 1:
       n.append((max(0,HP-HARD_MODE), MANA-173+RECHARGE_EFFECT, max(0,BOSS_HP-POISON_EFFECT), max(0,SHIELD_LEFT-1), POISSON_DURATION, max(0,RECHARGE_LEFT-1), not PLAYER_TURN,COST+173))

     #if cast Recharge:
     if RECHARGE_LEFT <= 1:
       n.append((max(0,HP-HARD_MODE), MANA-229+RECHARGE_EFFECT, max(0,BOSS_HP-POISON_EFFECT), max(0,SHIELD_LEFT-1), max(0,POISON_LEFT-1), RECHARGE_DURATION, not PLAYER_TURN, COST+229))

   if BOSS_TURN:
     n.append((max(0,HP-max(1,BOSS_DAMAGE-ARMOR_EFFECT)), MANA+RECHARGE_EFFECT, max(0,BOSS_HP-POISON_EFFECT), max(0,SHIELD_LEFT-1), max(0,POISON_LEFT-1), max(0,RECHARGE_LEFT-1), not PLAYER_TURN,COST))

   n = [x for x in n if is_valid(x)]

   if n != []:
     return random.choice(n)

   return None
   
def do_run(BOSS_HP_START, BOSS_DAMAGE, HARD_MODE, N):

  HP_START = 50
  MANA_START = 500

  start = (HP_START, MANA_START, BOSS_HP_START, 0, 0, 0, True, 0)
  min_cost = 100000

  for i in range(N):
    current_state = start
    while True:
      if current_state == None or is_done(current_state) or bad_cost(current_state, min_cost):
        break
       
      current_state = neighbors(current_state, BOSS_DAMAGE, HARD_MODE)
 
    if current_state != None and is_win(current_state):
       (HP, MANA, BOSS_HP, SHIELD_LEFT, POISON_LEFT, RECHARGE_LEFT, PLAYER_TURN, COST) = current_state
       min_cost = min(min_cost, COST)

  print(min_cost)

do_run(55, 8, 0, 10**4)
do_run(55, 8, 1, 10**5)
