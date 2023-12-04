#m = [[0]]*137
#with open("input.txt","r") as file:
#  lines = file.readlines()
#  for i,line in enumerate(lines):
#    line = line.rstrip('\n')
#    m[i] = list(line)
s = list('...>>>>>...')

print(''.join(s))
o = list('.' * len(s))
for i,c in enumerate(s):
  if c == '>':
    if i < len(s) and s[i+1] == '.':
      o[i+1] = '>'
    else:
      o[i] = '>'
print(''.join(o))

s = o.copy()
o = list('.' * len(s))
for i,c in enumerate(s):
  if c == '>':
    if i < len(s) and s[i+1] == '.':
      o[i+1] = '>'
    else:
      o[i] = '>'
print(''.join(o))

s = '''
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
'''
s = s.lstrip('\n').rstrip('\n')

lines = s.split('\n')
for i,_ in enumerate(lines):
  map(lambda x : x[i], lines)

s = ['v', '.', '>', '>', 'v', '>', '.', 'v', '.']
o = list('.' * len(s))
for i,c in enumerate(s):
  o[i] = c
  if c == '.':
    if i > 0 and s[i-1] == 'v':
      o[i] = 'v'
      o[i-1] = '.'

print(''.join(s))
print(''.join(o))
