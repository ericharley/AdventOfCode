import re
from collections import defaultdict

lines = open('input.txt').read().strip().splitlines()

# sort the input by date stamp
new_lines = []
for line in lines:
  year,month,day,hour,m,rest = re.findall(r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\](.*)$', line)[0]
  new_lines.append( (tuple(map(int,(year,month,day,hour,m))),line) )

lines = [y for x,y in sorted(new_lines)]

# parse the sorted input
record = defaultdict( lambda : defaultdict(lambda:'.'))

for line in lines:
  year,month,day,hour,m = re.findall(r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\]', line)[0]
  if 'Guard' in line:
    id = re.findall(r'Guard #(\d+)',line)[0]
    record[month,day,id][m] = '.'
  elif 'falls asleep' in line:
    for i in range(int(m),60):
      record[month,day,id][i] = '#'
  elif 'wakes up' in line:
    for i in range(int(m),60):
      record[month,day,id][i] = '.'

# Part 1
# Total minutes asleep by guard
asleep = defaultdict(int)
for month,day,id in record:
  asleep[id] += list(record[month,day,id].values()).count('#')

# Guard with most minutes asleep
max_id = max(asleep, key=asleep.get)

# Most frequent minute for guard to be asleep
c = defaultdict(int)
for month,day,id in record:
  if id == max_id:
    for k,v in record[month,day,id].items():
      if v == '#':
        c[k] += 1

max_min = max(c, key=c.get)

print(int(max_id)*int(max_min))

# Part 2
# frequency of (guard,minute) asleep

c = defaultdict(int)
for month,day,id in record:
  for m,v in record[month,day,id].items():
    if v == '#':
      c[id,m] += 1

id,m = max(c, key=c.get)
print(int(id)*int(m))
