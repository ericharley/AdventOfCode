from itertools import accumulate

lines = open('input.txt').read().strip().replace('R','+').replace('L','-').split()
steps = list(map(int, lines))

# Part 1
print( sum( [(x % 100 == 0) for x in accumulate([50]+steps)]) )

# Part 2
steps2 = [[+1 if step > 0 else -1]*abs(step) for step in steps]
steps2 = [x for sub in steps2 for x in sub]
steps2 = list(accumulate(steps2, initial=50))

hits = sum([(x%100)==0 for x in steps2])

print(hits)