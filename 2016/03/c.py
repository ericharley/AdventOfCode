lines = open('input.txt').read().strip().split('\n')
grid = list(map(lambda x : list(map(int, x.split())), lines))

def is_possible(n):
  return (n[0]+n[1] > n[2]) and (n[0]+n[2] > n[1]) and (n[1]+n[2] > n[0])

# Part 1
print(sum([is_possible(n) for n in grid]))

# Part 2
grid = list(zip(*grid))

possible = 0
for i in range(3):
  tris = list(zip(*[grid[i][j::3] for j in range(3)]))
  possible += sum([is_possible(n) for n in tris])

print(possible)
