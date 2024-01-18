from itertools import groupby

def look_and_say(n, s):
    for i in range(n):
        s = ''.join([str(len(list(g))) + str(k) for k, g in groupby(s)])
    return s

# Input
s = '1321131112'

# Part 1
print( len(look_and_say(40, s)))

# Part 2
print( len(look_and_say(50, s)))
