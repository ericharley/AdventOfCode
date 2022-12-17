from random import random, randrange
from time import time
t0 = time()

test = False

#Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
#Valve BB has flow rate=13; tunnels lead to valves CC, AA
#Valve CC has flow rate=2; tunnels lead to valves DD, BB
#Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
#Valve EE has flow rate=3; tunnels lead to valves FF, DD
#Valve FF has flow rate=0; tunnels lead to valves EE, GG
#Valve GG has flow rate=0; tunnels lead to valves FF, HH
#Valve HH has flow rate=22; tunnel leads to valve GG
#Valve II has flow rate=0; tunnels lead to valves AA, JJ
#Valve JJ has flow rate=21; tunnel leads to valve II

n = {}
f = {}

if test:
 n['AA'] = ['DD','II','BB']
 f['AA'] = 0
 n['BB'] = ['CC','AA']
 f['BB'] = 13
 n['CC'] = ['DD','BB']
 f['CC'] = 2
 n['DD'] = ['CC','AA','EE']
 f['DD'] = 20
 n['EE'] = ['FF','DD']
 f['EE'] = 3
 n['FF'] = ['EE','GG']
 f['FF'] = 0
 n['GG'] = ['FF','HH']
 f['GG'] = 0
 n['HH'] = ['GG']
 f['HH'] = 22
 n['II'] = ['AA','JJ']
 f['II'] = 0
 n['JJ'] = ['II']
 f['JJ'] = 21
else:
 f['XC'] = 0
 n['XC'] = ['YK', 'AM']
 f['ME'] = 0
 n['ME'] = ['UU', 'SX']
 f['EP'] = 0
 n['EP'] = ['YS', 'QU']
 f['GR'] = 0
 n['GR'] = ['QZ', 'OG']
 f['FA'] = 0
 n['FA'] = ['DB', 'DP']
 f['UJ'] = 0
 n['UJ'] = ['XN', 'CH']
 f['QU'] = 0
 n['QU'] = ['EP', 'YK']
 f['OX'] = 19
 n['OX'] = ['RI', 'PV']
 f['VI'] = 0
 n['VI'] = ['WI', 'XN']
 f['IQ'] = 0
 n['IQ'] = ['QL', 'OG']
 f['XO'] = 0
 n['XO'] = ['GU', 'UI']
 f['IY'] = 0
 n['IY'] = ['VC', 'NT']
 f['YS'] = 24
 n['YS'] = ['EP']
 f['XN'] = 7
 n['XN'] = ['DG', 'UJ', 'VD', 'VI', 'OU']
 f['AM'] = 6
 n['AM'] = ['KA', 'NC', 'XC', 'TP', 'SI']
 f['IH'] = 8
 n['IH'] = ['TW', 'CH', 'WY', 'EC']
 f['ZR'] = 18
 n['ZR'] = ['RI']
 f['FP'] = 14
 n['FP'] = ['DP', 'UF']
 f['KA'] = 0
 n['KA'] = ['VC', 'AM']
 f['NC'] = 0
 n['NC'] = ['UI', 'AM']
 f['EC'] = 0
 n['EC'] = ['IH', 'GU']
 f['DG'] = 0
 n['DG'] = ['AA', 'XN']
 f['RI'] = 0
 n['RI'] = ['OX', 'ZR']
 f['NJ'] = 0
 n['NJ'] = ['YK', 'TW']
 f['OG'] = 12
 n['OG'] = ['GR', 'WY', 'IQ', 'UE']
 f['IB'] = 0
 n['IB'] = ['VB', 'UU']
 f['RP'] = 0
 n['RP'] = ['UI', 'OU']
 f['OU'] = 0
 n['OU'] = ['XN', 'RP']
 f['NT'] = 0
 n['NT'] = ['IY', 'AA']
 f['MN'] = 0
 n['MN'] = ['LX', 'VC']
 f['SI'] = 0
 n['SI'] = ['AM', 'AA']
 f['VB'] = 0
 n['VB'] = ['KT', 'IB']
 f['UI'] = 4
 n['UI'] = ['YI', 'XO', 'LX', 'NC', 'RP']
 f['DL'] = 0
 n['DL'] = ['GU', 'UE']
 f['CH'] = 0
 n['CH'] = ['UJ', 'IH']
 f['WI'] = 0
 n['WI'] = ['VI', 'VC']
 f['GU'] = 11
 n['GU'] = ['EC', 'XO', 'DL', 'SX']
 f['KT'] = 17
 n['KT'] = ['PV', 'VB']
 f['TW'] = 0
 n['TW'] = ['IH', 'NJ']
 f['UE'] = 0
 n['UE'] = ['DL', 'OG']
 f['PV'] = 0
 n['PV'] = ['KT', 'OX']
 f['DP'] = 0
 n['DP'] = ['FP', 'FA']
 f['TP'] = 0
 n['TP'] = ['VD', 'AM']
 f['YI'] = 0
 n['YI'] = ['AA', 'UI']
 f['LX'] = 0
 n['LX'] = ['UI', 'MN']
 f['QZ'] = 0
 n['QZ'] = ['GR', 'UU']
 f['DB'] = 23
 n['DB'] = ['FA']
 f['SX'] = 0
 n['SX'] = ['ME', 'GU']
 f['QL'] = 0
 n['QL'] = ['AA', 'IQ']
 f['YK'] = 16
 n['YK'] = ['NJ', 'XC', 'QU']
 f['VC'] = 5
 n['VC'] = ['UF', 'KA', 'WI', 'IY', 'MN']
 f['VD'] = 0
 n['VD'] = ['TP', 'XN']
 f['WY'] = 0
 n['WY'] = ['IH', 'OG']
 f['AA'] = 0
 n['AA'] = ['YI', 'DG', 'QL', 'NT', 'SI']
 f['UF'] = 0
 n['UF'] = ['VC', 'FP']
 f['UU'] = 15
 n['UU'] = ['QZ', 'IB', 'ME']

max_pressure = 0
iter_max = 10000000

for i in range(iter_max):

  if i % (iter_max // 100) == 0:
    print(i/iter_max)

  previous = 'AA'
  current = 'AA'
  opened = set()
  minutes = 30
  pressure = 0

  while minutes >= 0:

    # if we're currently in a room that can be opened, then 85% of the time just open it and move
    if (f[current] != 0) and (current not in opened) and (random() > 0.15):
      minutes -= 1
      opened.add(current)
      pressure += minutes*f[current]

    # neighborhood of valves to move to from current
    choices = n[current].copy()

    # 95% of the time, do not double back
    if (random() > 0.05) and (previous in choices) and len(choices) > 1:
      choices.remove(previous)
    
    # move to the next valve
    previous = current
    current = choices[randrange(0,len(choices))]
    minutes -=1

  # at the end of this trip, see if we did alright
  if pressure > max_pressure:
     max_pressure = pressure
     print(i, max_pressure, time()-t0)
