import numpy as np

# data = np.loadtxt("test.txt", dtype=int, delimiter=",")
data = np.loadtxt("input.txt", dtype=int, delimiter=",")

# Part 1
# Geometric median, Weber problem
v = np.median(data)
print( int(np.sum(abs(data - v))) )

# Part 2
# Solution is near the mean +/- 0.5
w = lambda x: (x * (x+1)//2)
f = lambda x: int( w(abs(data-x)).sum() )

a = np.mean(data)
v1 = int(np.floor(a))
v2 = int(np.ceil(a))

print( np.min( [f(v1), f(v2)] ) )
