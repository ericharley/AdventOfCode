lines = open('input.txt').read().strip().split('\n')
columns = list(zip(*lines))

output = ['','']
for col in columns:
  m = {c : col.count(c) for c in col}
  max_v,min_v = max(m.values()), min(m.values())
  output[0] += [c for c,v in m.items() if v == max_v][0]
  output[1] += [c for c,v in m.items() if v == min_v][0]

# Part 1
print(output[0])

# Part 2
print(output[1])
