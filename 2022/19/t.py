from collections import namedtuple
from random import random, randrange
from time import time

t0 = time()

Cost = namedtuple('Cost', ['ore', 'clay', 'obsidian'])
Resources = namedtuple('Resources', ['ore', 'clay', 'obsidian','ore_robot','clay_robot','obsidian_robot','geode_robot', 'geode'])
	
cost = {}
cost['ore_robot'] = Cost(4,0,0)
cost['clay_robot'] = Cost(2,0,0)
cost['obsidian_robot'] = Cost(3,14,0)
cost['geode_robot'] = Cost(2,0,7)

robots = ['ore_robot','clay_robot','obsidian_robot','geode_robot']

time_limit = 24

max_geode = 0
iter_max = 1
#0000

def print_min(r_start, r_end, did_make):
 if did_make['ore_robot']:
  print(f"Spend {cost['ore_robot'].ore} ore to start building a ore-collecting robot.")
 if did_make['clay_robot']:
  print(f"Spend {cost['clay_robot'].ore} ore to start building a clay-collecting robot.")
 if did_make['obsidian_robot']:
  print(f"Spend {cost['obsidian_robot'].ore} ore and {cost['obsidian_robot'].clay} clay to start building an obsidian-collecting robot.")
 if did_make['geode_robot']:
  print(f"Spend {cost['geode_robot'].ore} ore and {cost['geode_robot'].obsidian} obsidian to start building a geode-cracking robot.")

 if r_start.ore_robot > 0:
  print(f'{r_start.ore_robot} ore-collecting robot collects {r_start.ore_robot} core; you now have {r_end.ore} ore.')
 if r_start.clay_robot > 0:
  print(f'{r_start.clay_robot} clay-collecting robots collect {r_start.clay_robot} clay; you now have {r_end.clay} clay.')
 if r_start.obsidian_robot > 0:
  print(f'{r_start.obsidian_robot} obsidian-collecting robots collect {r_start.obsidian_robot} obsidian; you now have {r_end.obsidian} obsidian.')
 if r_start.geode_robot > 0:
  print(f'{r_start.geode_robot} geode-cracking robot cracks {r_start.geode_robot} geode; you now have {r_end.geode} open geodes.')

 if did_make['ore_robot']:
  print(f'The new ore-collecting robot is ready; you now have {r_end.ore_robot} of them.')
 if did_make['clay_robot']:
  print(f'The new clay-collecting robot is ready; you now have {r_end.clay_robot} of them.')
 if did_make['obsidian_robot']:
  print(f'The new obsidian-collecting robot is ready; you now have {r_end.obsidian_robot} of them.')
 if did_make['geode_robot']:
  print(f'The new geode-cracking robot is ready; you now have {r_end.geode_robot} of them.')


actions = {}
actions[3] = ['clay']
actions[5] = ['clay']
actions[7] = ['clay']
actions[11] = ['obsidian']
actions[12] = ['clay']
actions[15] = ['obsidian']
actions[18] = ['geode']
actions[21] = ['geode']

for i in range(iter_max):

#  if i % (iter_max // 100) == 0:
#    print(i/iter_max)

  minutes = time_limit
  # start with exactly one ore robot
  resources = Resources(0, 0, 0, 1, 0, 0, 0, 0)
  print(resources)
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

    if the_minute in actions:
       if 'ore' in actions[the_minute]:
         did_make['ore_robot'] = True
         ore_spent = cost['ore_robot'].ore
         clay_spent = cost['ore_robot'].clay
         obsidian_spent = cost['ore_robot'].obsidian
       if 'clay' in actions[the_minute]:
         did_make['clay_robot'] = True
         ore_spent = cost['clay_robot'].ore
         clay_spent = cost['clay_robot'].clay
         obsidian_spent = cost['clay_robot'].obsidian
       if 'obsidian' in actions[the_minute]:
         did_make['obsidian_robot'] = True
         ore_spent = cost['obsidian_robot'].ore
         clay_spent = cost['obsidian_robot'].clay
         obsidian_spent = cost['obsidian_robot'].obsidian
       if 'geode' in actions[the_minute]:
         did_make['geode_robot'] = True
         ore_spent = cost['geode_robot'].ore
         clay_spent = cost['geode_robot'].clay
         obsidian_spent = cost['geode_robot'].obsidian
	   
    rr = resources
    new_resources = Resources(rr.ore + rr.ore_robot - ore_spent,
                              rr.clay + rr.clay_robot - clay_spent,
                              rr.obsidian + rr.obsidian_robot - obsidian_spent,
                              rr.ore_robot      + (1 if did_make['ore_robot']      else 0),
                              rr.clay_robot     + (1 if did_make['clay_robot']     else 0), 
                              rr.obsidian_robot + (1 if did_make['obsidian_robot'] else 0),
                              rr.geode_robot    + (1 if did_make['geode_robot']    else 0),
                              rr.geode + rr.geode_robot)

 
    print(f'== Minute {the_minute}  ==')
    print_min(resources, new_resources, did_make)
    print()

    resources = new_resources

    minutes -= 1
#    print(resources)

#  print(resources)

