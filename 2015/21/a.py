from itertools import combinations

#Input
# Hit Points: 104
# Damage: 8
# Armor: 1
#
#You must buy exactly one weapon;
#no dual-wielding. Armor is optional, but you can't use more than one.
#You can buy 0-2 rings (at most one for each hand).
#
#You must use any items you buy.
#
#The shop only has one of each item, 
#so you can't buy, for example, two rings of Damage +3.

#         Cost, Damage, Armor
weapons = {
'Dagger'    :( 8, 4, 0),
'Shortsword':(10, 5, 0),
'Warhammer' :(25, 6, 0),
'Longsword' :(40, 7, 0),
'Greataxe'  :(74, 8, 0),
}
armors = {
'No armor'   : (0,0,0),
'Leather'    : ( 13, 0, 1),
'Chainmail'  : ( 31, 0, 2),
'Splintmail' : ( 53, 0, 3),
'Bandedmail' : ( 75, 0, 4),
'Platemail'  : (102, 0, 5),
}
rings = {
'No Ring'  : (0,0,0),
'Damage +1' : ( 25,  1, 0),
'Damage +2' : ( 50,  2, 0),
'Damage +3' : (100,  3, 0),
'Defense +1': ( 20,  0, 1),
'Defense +2': ( 40,  0, 2),
'Defense +3': ( 80,  0, 3),
}
combos = {}
# buy one weapon
# buy zero or one armor
# Buy 0,1,2 rings
#
# damage score and armor score are 0
# You have 100 hit points.
#
for weapon in weapons:
  for armor in armors:
    for r1 in rings:
      for r2 in rings:
        if r1 == r2 and r1 != "No Ring":
          continue
        if r1 < r2 :
          combos[(weapon, armor, r1, r2)] = 1
        else:
          combos[(weapon, armor, r2, r1)] = 1

win = {}
lose = {}

def sim(weapon, armor, r1, r2):

#  You have 100 hit points.
  hp = 100
  damage = weapons[weapon][1] + rings[r1][1] + rings[r2][1]
  armor = armors[armor][2] + rings[r1][2] + rings[r2][2]

  boss_hp = 104
  boss_damage = 8
  boss_armor = 1

  while hp > 0 and boss_hp > 0:
    d = (damage - boss_armor) if (damage - boss_armor) > 0 else 1
    boss_hp = boss_hp - d if boss_hp - d > 0 else 0
#    print(f'The player deals {damage}-{boss_armor} = {d} damage; the boss goes down to {boss_hp} hit points.')

    if boss_hp == 0:
      break

    d = (boss_damage - armor) if (boss_damage - armor) > 0 else 1
    hp = hp - d if hp - d > 0 else 0
#    print(f'The boss deals {boss_damage}-{armor} = {d} damage; the player goes down to {hp} hit points.')

    if hp == 0:
      break

  if boss_hp == 0:
    return True
  else:
    return False

def cost(weapon, armor, r1, r2):
  return weapons[weapon][0] + rings[r1][0] + rings[r2][0] + armors[armor][0]

for weapon, armor, r1, r2 in combos:
  if sim(weapon, armor, r1, r2):
    win[(weapon, armor, r1, r2)] = cost(weapon, armor, r1, r2)
  else:
    lose[(weapon, armor, r1, r2)] = cost(weapon, armor, r1, r2)

print(min(win.values()))
print(max(lose.values()))

#for weapon, armor, r1, r2 in win:
#  print(win[(weapon, armor, r1, r2)], weapon, armor, r1, r2)
#
#for weapon, armor, r1, r2 in lose:
#  print(lose[(weapon, armor, r1, r2)], weapon, armor, r1, r2)
