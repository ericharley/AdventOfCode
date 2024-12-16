import re
from pulp import LpProblem, LpVariable, LpMinimize, LpStatus, value, apis

lines = open('input.txt').read().strip().split('\n\n')
data = [list(map(int, re.findall(r'\d+', x))) for x in lines]

total = 0
for AX,AY,BX,BY,PX,PY in data:
  
  problem = LpProblem("Integer_Linear_Equations", LpMinimize)
 
  X = LpVariable("X", lowBound=0, cat="Integer")
  Y = LpVariable("Y", lowBound=0, cat="Integer")
  
  problem += 3 * X + Y
  
  problem += AX * X + BX * Y == PX
  problem += AY * X + BY * Y == PY
  
  problem.solve(apis.PULP_CBC_CMD(msg=False))

  if LpStatus[problem.status] == 'Optimal':
    total += value(problem.objective)

print(total)