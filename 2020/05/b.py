lines = open('input5.txt').readlines()

t = str.maketrans('FBLR','0101')
h = set( int(s.translate(t),2) for s in lines )

# Part 1
print(max(h))

# Part 2
print( next(i for i in range(min(h), max(h)) if i not in h) )
