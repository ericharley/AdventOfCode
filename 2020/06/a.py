lines = open('input.txt').readlines()
data = ''.join(lines).strip().split('\n\n')
sets = [list(map(set, x.split('\n'))) for x in data]

# Part 1
print( sum(len(set.union(*s)) for s in sets) )

# Part 2
print( sum(len(set.intersection(*s)) for s in sets) )
