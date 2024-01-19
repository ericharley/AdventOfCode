import copy
import heapq

from itertools import combinations

def is_valid(move,floors,E):
  new_floor, objects = move

  if not ( 0 <= new_floor < 4 ):
    return False

  # can only move one floor at a time
  if abs(new_floor - E) != 1:
    return False

  # elevator must have at least one thing, no more than 2
  if len(objects) > 2 or len(objects) == 0:
    return False

  # if microchip in the move, then floor it's moving to must contain no generators
  #   or it must travel to a floor that contains its generator
  floor_gens = {obj for obj in floors[new_floor] if 'G' in obj}
  floor_micros = {obj for obj in floors[new_floor] if 'M' in obj}

  moving_micros = {x for x in objects if 'M' in x}
  moving_gens = {x for x in objects if 'G' in x}

  if len(floor_gens|moving_gens) != 0:
    for micro in (floor_micros | moving_micros):
      corresponding_gen = micro[0] + 'G'
      if corresponding_gen not in (floor_gens | moving_gens):
        return False

  # if we're moving a generator, we can't separate it from its micro if that would leave an unpaired micro
  remaining = floors[E] - moving_gens
  remaining_micros = {x for x in remaining if 'M' in x}
  remaining_gens = {x for x in remaining if 'G' in x}
  if len(remaining_gens) > 0:
    for micro in remaining_micros:
      corresponding_gen = micro[0] + 'G'
      if corresponding_gen not in remaining_gens:
        return False

  return True

def get_moves(floors, E):
  moves = []
  for haul in combinations(floors[E], 1):
    moves.append((E+1, set(haul)))
    moves.append((E-1, set(haul)))
  for haul in combinations(floors[E], 2):
    moves.append((E+1, set(haul)))
    moves.append((E-1, set(haul)))

  moves = [x for x in moves if is_valid(x, floors, E)]
  return moves

def apply_move(floors,E,move):
  new_floor, objects = move
  new_floors = copy.deepcopy(floors)
  new_floors[E] = set(floors[E] - objects)
  new_floors[new_floor] = set(floors[new_floor] | objects)

  return new_floors, new_floor

def t(floors):
  return tuple(map(tuple,floors))

def doit(floors):
  E = 0
  N = sum([len(x) for x in floors])
  def is_goal(floors):
    return len(floors[3]) == N

  visited = {}
  q = []

  start = (0,floors,E)
  visited[(t(floors),E)] = True
  heapq.heappush(q, (0,start))

  while q:

    _,(k,floors,E) = heapq.heappop(q)
    if is_goal(floors):
      print(k)
      break

    for move in get_moves(floors,E):
      new_floors,new_E = apply_move(floors,E,move)
      if (t(new_floors),new_E) not in visited:
        visited[(t(new_floors),new_E)] = True
        priority = k - len(new_floors[3])*10
        heapq.heappush(q, (priority,(k+1,new_floors,new_E)))

## Test
#floors = [{'HM','LM'},{'HG'},{'LG'},set()]
#doit(floors)

# 1
floors = [{'TG','TM','PG','SG'},{'PM','SM'},{'AG','AM','RG','RM'},set()]
doit(floors)

# 2
floors = [{'DM','DG','EM','EG','TG','TM','PG','SG'},{'PM','SM'},{'AG','AM','RG','RM'},set()]
doit(floors)
