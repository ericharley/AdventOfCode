#filename = 'test.txt'
filename = 'input.txt'

instructions, parts = open(filename).read().split('\n\n')

instructions = instructions.split('\n')
parts = parts.split('\n')


rules = {}
for s in instructions:
  rule_name = s.split('{')[0]
  rule_list = s.split('{')[1].split(',')[:-1]
  otherwise = s.split('{')[1].split(',')[-1][:-1]

  parsed_rule_list = []
  for rule in rule_list:
    r, go = rule.split(':')
    var,op,val = r[0],r[1],r[2:]
    val = int(val)
    parsed_rule_list.append((var,op,val,go))

  rules[rule_name] = (parsed_rule_list, otherwise)


def apply_rule(rule, p):

  rule_list = rule[0]
  otherwise = rule[1]

  for var,op,val,go in rule_list:
    if eval(f'{p[var]} {op} {val}') :
      return go

  else:
    return otherwise

parts.pop()
total = 0

for p in parts:
 
 m = eval(p.replace('=',':').replace(':','\':').replace('{','{\'').replace(',',',\''))
 
 current_rule = 'in'

 while True:
   next_rule = apply_rule(rules[current_rule], m)

   if next_rule == 'A':
     total += sum(m.values())
     break
   elif next_rule == 'R':
     break
#   else:
#     print(current_rule ,':', rules[current_rule])

   current_rule = next_rule

# print()

print(total)
