from collections import namedtuple
from random import random, randrange
from time import time

import sys

if __name__ == "__main__":
#    print(f"Arguments count: {len(sys.argv)}")
#    for i, arg in enumerate(sys.argv):
#        print(f"Argument {i:>6}: {arg}")
  if len(sys.argv) == 2:
    BP = int(sys.argv[1])
  else:
    print('Enter BP #: ')
    BP = int(input())


t0 = time()

Cost = namedtuple('Cost', ['ore', 'clay', 'obsidian'])
Resources = namedtuple('Resources', ['ore', 'clay', 'obsidian','ore_robot','clay_robot','obsidian_robot','geode_robot', 'geode'])
	
cost = {}
##BP 1
#cost['ore_robot'] = Cost(4,0,0)
#cost['clay_robot'] = Cost(4,0,0)
#cost['obsidian_robot'] = Cost(3,5,0)
#cost['geode_robot'] = Cost(3,0,18)

#BP 1
if BP == 1:
 cost['ore_robot'] = Cost(4,0,0)
 cost['clay_robot'] = Cost(4,0,0)
 cost['obsidian_robot'] = Cost(3,5,0)
 cost['geode_robot'] = Cost(3,0,18)

#BP 2
if BP == 2:
 cost['ore_robot'] = Cost(4,0,0)
 cost['clay_robot'] = Cost(4,0,0)
 cost['obsidian_robot'] = Cost(4,16,0)
 cost['geode_robot'] = Cost(2,0,15)

#BP 3
if BP == 3:
 cost['ore_robot'] = Cost(3,0,0)
 cost['clay_robot'] = Cost(4,0,0)
 cost['obsidian_robot'] = Cost(4,19,0)
 cost['geode_robot'] = Cost(4,0,11)

#BP 4
if BP == 4:
 cost['ore_robot'] = Cost(4,0,0)
 cost['clay_robot'] = Cost(3,0,0)
 cost['obsidian_robot'] = Cost(2,13,0)
 cost['geode_robot'] = Cost(2,0,9)

#BP 5
if BP == 5:
 cost['ore_robot'] = Cost(4,0,0)
 cost['clay_robot'] = Cost(4,0,0)
 cost['obsidian_robot'] = Cost(2,14,0)
 cost['geode_robot'] = Cost(4,0,15)

#BP 6
if BP == 6:
 cost['ore_robot'] = Cost(4,0,0)
 cost['clay_robot'] = Cost(3,0,0)
 cost['obsidian_robot'] = Cost(3,10,0)
 cost['geode_robot'] = Cost(2,0,10)

#BP 7
if BP == 7:
 cost['ore_robot'] = Cost(2,0,0)
 cost['clay_robot'] = Cost(4,0,0)
 cost['obsidian_robot'] = Cost(4,16,0)
 cost['geode_robot'] = Cost(4,0,17)

#BP 8
if BP == 8:
 cost['ore_robot'] = Cost(2,0,0)
 cost['clay_robot'] = Cost(4,0,0)
 cost['obsidian_robot'] = Cost(3,19,0)
 cost['geode_robot'] = Cost(4,0,12)

#BP 9
if BP == 9:
 cost['ore_robot'] = Cost(3,0,0)
 cost['clay_robot'] = Cost(3,0,0)
 cost['obsidian_robot'] = Cost(3,17,0)
 cost['geode_robot'] = Cost(2,0,13)

#BP 10
if BP == 10:
 cost['ore_robot'] = Cost(3,0,0)
 cost['clay_robot'] = Cost(4,0,0)
 cost['obsidian_robot'] = Cost(4,8,0)
 cost['geode_robot'] = Cost(2,0,10)

#BP 11
if BP == 11:
 cost['ore_robot'] = Cost(4,0,0)
 cost['clay_robot'] = Cost(3,0,0)
 cost['obsidian_robot'] = Cost(2,7,0)
 cost['geode_robot'] = Cost(3,0,8)

#BP 12
if BP == 12:
 cost['ore_robot'] = Cost(3,0,0)
 cost['clay_robot'] = Cost(4,0,0)
 cost['obsidian_robot'] = Cost(3,18,0)
 cost['geode_robot'] = Cost(4,0,16)

#BP 13
if BP == 13:
 cost['ore_robot'] = Cost(4,0,0)
 cost['clay_robot'] = Cost(3,0,0)
 cost['obsidian_robot'] = Cost(2,20,0)
 cost['geode_robot'] = Cost(3,0,9)

#BP 14
if BP == 14:
 cost['ore_robot'] = Cost(4,0,0)
 cost['clay_robot'] = Cost(3,0,0)
 cost['obsidian_robot'] = Cost(4,6,0)
 cost['geode_robot'] = Cost(3,0,11)

#BP 15
if BP == 15:
 cost['ore_robot'] = Cost(4,0,0)
 cost['clay_robot'] = Cost(4,0,0)
 cost['obsidian_robot'] = Cost(2,16,0)
 cost['geode_robot'] = Cost(4,0,16)

#BP 16
if BP == 16:
 cost['ore_robot'] = Cost(4,0,0)
 cost['clay_robot'] = Cost(3,0,0)
 cost['obsidian_robot'] = Cost(4,5,0)
 cost['geode_robot'] = Cost(3,0,19)

#BP 17
if BP == 17:
 cost['ore_robot'] = Cost(4,0,0)
 cost['clay_robot'] = Cost(4,0,0)
 cost['obsidian_robot'] = Cost(3,5,0)
 cost['geode_robot'] = Cost(4,0,11)

#BP 18
if BP == 18:
 cost['ore_robot'] = Cost(4,0,0)
 cost['clay_robot'] = Cost(3,0,0)
 cost['obsidian_robot'] = Cost(4,18,0)
 cost['geode_robot'] = Cost(3,0,13)

#BP 19
if BP == 19:
 cost['ore_robot'] = Cost(3,0,0)
 cost['clay_robot'] = Cost(3,0,0)
 cost['obsidian_robot'] = Cost(3,9,0)
 cost['geode_robot'] = Cost(3,0,7)

#BP 20
if BP == 20:
 cost['ore_robot'] = Cost(2,0,0)
 cost['clay_robot'] = Cost(3,0,0)
 cost['obsidian_robot'] = Cost(2,14,0)
 cost['geode_robot'] = Cost(3,0,20)

#BP 21
if BP == 21:
 cost['ore_robot'] = Cost(2,0,0)
 cost['clay_robot'] = Cost(4,0,0)
 cost['obsidian_robot'] = Cost(2,20,0)
 cost['geode_robot'] = Cost(2,0,17)

#BP 22
if BP == 22:
 cost['ore_robot'] = Cost(4,0,0)
 cost['clay_robot'] = Cost(4,0,0)
 cost['obsidian_robot'] = Cost(4,14,0)
 cost['geode_robot'] = Cost(3,0,16)

#BP 23
if BP == 23:
 cost['ore_robot'] = Cost(3,0,0)
 cost['clay_robot'] = Cost(3,0,0)
 cost['obsidian_robot'] = Cost(2,20,0)
 cost['geode_robot'] = Cost(3,0,18)

#BP 24
if BP == 24:
 cost['ore_robot'] = Cost(2,0,0)
 cost['clay_robot'] = Cost(2,0,0)
 cost['obsidian_robot'] = Cost(2,20,0)
 cost['geode_robot'] = Cost(2,0,14)

#BP 25
if BP == 25:
 cost['ore_robot'] = Cost(2,0,0)
 cost['clay_robot'] = Cost(4,0,0)
 cost['obsidian_robot'] = Cost(4,16,0)
 cost['geode_robot'] = Cost(3,0,13)

#BP 26
if BP == 26:
 cost['ore_robot'] = Cost(3,0,0)
 cost['clay_robot'] = Cost(3,0,0)
 cost['obsidian_robot'] = Cost(3,9,0)
 cost['geode_robot'] = Cost(2,0,10)

#BP 27
if BP == 27:
 cost['ore_robot'] = Cost(4,0,0)
 cost['clay_robot'] = Cost(3,0,0)
 cost['obsidian_robot'] = Cost(3,20,0)
 cost['geode_robot'] = Cost(2,0,19)

#BP 28
if BP == 28:
 cost['ore_robot'] = Cost(3,0,0)
 cost['clay_robot'] = Cost(3,0,0)
 cost['obsidian_robot'] = Cost(3,15,0)
 cost['geode_robot'] = Cost(2,0,8)

#BP 29
if BP == 29:
 cost['ore_robot'] = Cost(3,0,0)
 cost['clay_robot'] = Cost(4,0,0)
 cost['obsidian_robot'] = Cost(4,18,0)
 cost['geode_robot'] = Cost(4,0,12)

#BP 30
if BP == 30:
 cost['ore_robot'] = Cost(2,0,0)
 cost['clay_robot'] = Cost(2,0,0)
 cost['obsidian_robot'] = Cost(2,10,0)
 cost['geode_robot'] = Cost(2,0,11)




robots = ['ore_robot','clay_robot','obsidian_robot','geode_robot']

time_limit = 32

max_geode = 0
iter_max = 1000000

for i in range(iter_max):

  minutes = time_limit
  # start with exactly one ore robot
  resources = Resources(0, 0, 0, 1, 0, 0, 0, 0)

  while minutes > 0:

    the_minute = time_limit-minutes+1

    did_make = {}
    for i in ['ore_robot','clay_robot','obsidian_robot','geode_robot']:
      did_make[i] = False

    can_make = {}
    for i in ['ore_robot','clay_robot','obsidian_robot','geode_robot']:
      can_make[i] = False
      if (cost[i].ore <= resources.ore) and (cost[i].clay <= resources.clay) and (cost[i].obsidian <= resources.obsidian):
        can_make[i] = True
 
    ore_spent = 0
    clay_spent = 0
    obsidian_spent = 0

    possible_actions = {x for x in can_make if can_make[x]}
    action = ''
    # if we can make a robot, then 95% of the time make it
    if possible_actions and (random() > 0.05):
      choices = list(possible_actions)
      if 'geode_robot' in choices :
        action = 'geode_robot'
      else:
        action = choices[randrange(0,len(choices))]

      # {'ore_robot': True, 'clay_robot': True, 'obsidian_robot': False, 'geode_robot': False}
      did_make[action] = True
      ore_spent = cost[action].ore 
      clay_spent = cost[action].clay
      obsidian_spent = cost[action].obsidian

    rr = resources
    new_resources = Resources(rr.ore + rr.ore_robot - ore_spent,
                              rr.clay + rr.clay_robot - clay_spent,
                              rr.obsidian + rr.obsidian_robot - obsidian_spent,
                              rr.ore_robot      + (1 if did_make['ore_robot']      else 0),
                              rr.clay_robot     + (1 if did_make['clay_robot']     else 0), 
                              rr.obsidian_robot + (1 if did_make['obsidian_robot'] else 0),
                              rr.geode_robot    + (1 if did_make['geode_robot']    else 0),
                              rr.geode + rr.geode_robot)

    resources = new_resources

    minutes -= 1

  if resources.geode > max_geode:
    max_geode = resources.geode
    print(max_geode)

# print(max_geode)

