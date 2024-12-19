import re

lines = open('input.txt').read().strip().split('\n\n')
line = lines[0]
line = '((' + line.replace(', ',')|(') + '))*'
pattern = line
regex = re.compile(pattern)

line = lines[1]
data = line.split('\n')

t = 0

for string in data:
  if regex.fullmatch(string):
    # print(string)
    t += 1

print(t)
