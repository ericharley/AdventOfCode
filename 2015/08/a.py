import json

lines = open('input.txt').read().strip().split('\n')

a,b = 0,0
for line in lines:
  a += (len(line) - len(eval(line)))
  b += len(json.dumps(line)) - len(line)

print(a, b)
