import re

lines = open('input.txt').readlines()
data = ''.join(lines).strip().split('\n\n')

fields = {
    'byr':r'^(19[2-9][0-9]|200[0-2])$',
    'iyr':r'^(201[0-9]|2020)$',
    'eyr':r'^(202[0-9]|2030)$',
    'hgt':r'^((59|6\d|7[0-6])in|(1[5-8]\d|19[0-3])cm)$',
    'hcl':r'^#[\d|a-f]{6}$',
    'ecl':r'^(amb|blu|brn|gry|grn|hzl|oth)$',
    'pid':r'^\d{9}$',
}

a,b = 0,0

for record in data:
  d = eval('{'+"'" + record.replace('\n',' ').replace(':',"':'").replace(' ',"', '") + "'"+'}')

  if all(x in d for x in fields):
    a += 1
    if all(re.match(fields[x],d[x]) for x in fields):
      b += 1

print(a)
print(b)
