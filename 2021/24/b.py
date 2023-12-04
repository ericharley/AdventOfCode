import re

c = {}
c['w'] = 1
c['x'] = 1
c['y'] = 1
c['z'] = 1

def eval_prog(lines, get_input):
 s = {}

 s['w'] = 0
 s['x'] = 0
 s['y'] = 0
 s['z'] = 0

 for line in lines:
   line = line.rstrip('\n')
   p = r'(inp|add|mod|div|eql|mul) (w|x|y|z) ?(-?[0-9]+|w|x|y|z)?'
   m = re.match(p,line)
 #  print(f'{line} ->[{m[1]}],[{m[2]}],[{m[3]}]')
 
   op = m[1]
   a = m[2]
   v = m[3]
   if v and not v.isalpha():
     v = int(m[3])
   if op == 'inp':
     val = get_input()
     #print('got a ', val)
     s[a] = val
     print(f'{a}{c[a]} = {val}')
     c[a] += 1
   elif op == 'add':
     #print(line)
     #print(s[a])
     s[a] = s[a] + (s[v] if type(v) == str else v)
     #print(s[a])
     if type(v) == str :
       print(f'{a}{c[a]} = {a}{c[a]-1} + {v}{c[v]-1}')
       c[a] += 1
     else:
       print(f'{a}{c[a]} = {a}{c[a]-1} + {v}')
       c[a] += 1
   elif op == 'mul':
     #print(line)
     #print(s[a])
     s[a] = s[a] * (s[v] if type(v) == str else v)
     #print(s[a])
     if type(v) == str :
       print(f'{a}{c[a]} = {a}{c[a]-1} * {v}{c[v]-1}')
       c[a] += 1
     else:
       print(f'{a}{c[a]} = {a}{c[a]-1} * {v}')
       c[a] += 1
   elif op == 'div':
     #print(line)
     #print(s[a])
     s[a] = s[a] // (s[v] if type(v) == str else v)
     #print(s[a])
     if type(v) == str :
       print(f'{a}{c[a]} = {a}{c[a]-1} // {v}{c[v]-1}')
       c[a] += 1
     else:
       print(f'{a}{c[a]} = {a}{c[a]-1} // {v}')
       c[a] += 1
   elif op == 'mod':
     #print(line)
     #print(s[a])
     s[a] = s[a] % (s[v] if type(v) == str else v)
     #print(s[a])
     if type(v) == str :
       print(f'{a}{c[a]} = {a}{c[a]-1} % {v}{c[v]-1}')
       c[a] += 1
     else:
       print(f'{a}{c[a]} = {a}{c[a]-1} % {v}')
       c[a] += 1
   elif op == 'eql':
     #print(line)
     #print(s[a])
     s[a] = 1 if (s[a] == s[v] if type(v) == str else s[a] == v) else 0
     #print(s[a])
     if type(v) == str :
       print(f'{a}{c[a]} = int({a}{c[a]-1} == {v}{c[v]-1})')
       c[a] += 1
     else:
       print(f'{a}{c[a]} = int({a}{c[a]-1} == {v})')
       c[a] += 1
   else:
     print('ERROR')
     exit()

 return s

with open("input.txt","r") as file:
#with open("test.txt","r") as file:
   lines = file.readlines()

def get_input():
  global ptr
  val = int(in_num[ptr],26)
  ptr+=1
  return val

ptr = 0
in_num = f'13579246899999'
s = eval_prog(lines, get_input)
print(s)

