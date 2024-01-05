import re

lines = open('input.txt').read().strip().split('\n')

def support_tls(line):
  hypernet = []
  for s in re.findall(r'\[([a-z]+?)\]', line):
    hypernet.append(s)
    line = line.replace(s,'')
  supernet = line

  has_abba = False
  for a,b in re.findall(r'(?=(.)(.)\2\1)', supernet):
    if a == b:
      continue
    has_abba = True
    break

  for s in hypernet:
    for a,b in re.findall(r'(?=(.)(.)\2\1)', s):
      if a == b:
        continue
      return False

  return has_abba

def support_ssl(line):
  hypernet = []
  for s in re.findall(r'\[([a-z]+?)\]', line):
    hypernet.append(s)
    line = line.replace(s,'')
  supernet = line
  #supernet = line.split('[]')

  for a,b in re.findall(r'(?=(.)(.)\1)', supernet):
    if a == b:
      continue

    for s in hypernet:
      if (b+a+b) in s:
        return True
  else:
    return False

a_count = 0
b_count = 0
for line in lines:

  if support_ssl(line):
    #print(line)
    b_count += 1

  if support_tls(line):
    #print(line)
    a_count += 1

print(a_count)
print(b_count)

