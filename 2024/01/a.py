with open('input.txt') as file:
  lines = list(zip(*[map(int, line.split()) for line in file]))

# Part 1
lines = [sorted(col) for col in lines]
print( sum(abs(a-b) for a,b in zip(*lines)) )

# Part 2
print( sum(a*lines[1].count(a) for a in lines[0]) )
