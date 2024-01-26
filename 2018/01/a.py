dfs = [int(v) for v in open('input.txt').read().strip().split('\n')]
n = len(dfs)

# Part 1
print(sum(dfs))

# Part 2
seen = {}
f,i = 0,0
while f not in seen:
  seen[f] = 1
  f += dfs[i % n]
  i += 1

print(f)

