import numpy as np

# f = open("test.txt", "r")
f = open("input.txt", "r")
v = [int(x) for x in f.readline().rstrip('\n').split(',')]

a = np.array(v)
b = np.zeros(9, dtype=int)

for i in range(9):
  b[i] = np.sum( a == i )

A = np.zeros((9,9), dtype=int)
A[1,0] = 1
A[2,1] = 1
A[3,2] = 1
A[4,3] = 1
A[5,4] = 1
A[6,5] = 1
A[7,6] = 1
A[8,7] = 1
A[0,8] = 1
A[0,6] = 1
A = A.transpose()

num_steps = 80
print(np.sum( np.linalg.matrix_power(A, num_steps) @ b ) )

num_steps = 256
print(np.sum( np.linalg.matrix_power(A, num_steps) @ b ) )
