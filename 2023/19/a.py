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

#  print(parsed_rule_list)
#  print(rule_name, rule_list, otherwise)

#for rule in rules:
#  print(f'{rule} -> {rules[rule]}')

def apply_rule(rule, p):
  x,m,a,s = p

  rule_list = rule[0]
  otherwise = rule[1]

  for var,op,val,go in rule_list:
    if eval(f'{var} {op} {val}') :
      return go

  else:
    return otherwise

parts.pop()
total = 0
for p in parts:
 exec(p[1:-1].replace(',','\n'))
 # x, m, a, s

 current_rule = 'in'

 print(f'{p}: ', end='')

 print(current_rule,end='')
 while True:
   next_rule = apply_rule(rules[current_rule], (x,m,a,s))
   print(f' -> {next_rule}', end='')

   if next_rule == 'A':
     print()
     total += x+m+a+s
     break
   elif next_rule == 'R':
     print()
     break
#   else:
#     print()
#     print(f'error: {p}, {next_rule}')
#     break  

   current_rule = next_rule

print(total)
