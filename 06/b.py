import numpy as np

# f = open("test.txt", "r")
f = open("input.txt", "r")
v = [int(x) for x in f.readline().rstrip('\n').split(',')]

a = np.array(v)
b = np.zeros(9, dtype=int)

for i in range(9):
  b[i] = np.sum( a == i )

A = np.zeros((9,9), dtype=int)
# A[to, from] = multiplier
# each fish clock goes from N to N-1
A[0,1] = 1
A[1,2] = 1
A[2,3] = 1
A[3,4] = 1
A[4,5] = 1
A[5,6] = 1
A[6,7] = 1
A[7,8] = 1
# fish at zero go to 6 and produce new fish at 8
A[6,0] = 1
A[8,0] = 1

# part 1
num_steps = 80
print(np.sum( np.linalg.matrix_power(A, num_steps) @ b ) )

# part 2
num_steps = 256
print(np.sum( np.linalg.matrix_power(A, num_steps) @ b ) )
