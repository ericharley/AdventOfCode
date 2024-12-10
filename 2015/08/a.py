import ast
import json

lines = open('input.txt').read().strip().split('\n')

a,b = 0,0
for line in lines:
  a += (len(line) - len(ast.literal_eval(line)))
  b += len(json.dumps(line)) - len(line)

# Part 1
print(a)

# Part 2
print(b)
