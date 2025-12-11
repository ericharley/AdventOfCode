from math import prod
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix

# ---------------------------
# 1. Read graph & build A
# ---------------------------
edges = []
nodes = set()

lines = open("input.txt").read().strip().splitlines()
for line in lines:
    frm, tos = line.split(": ")
    tos = tos.split()
    for to in tos:
        edges.append((frm, to))
        nodes.add(frm)
        nodes.add(to)

node_to_idx = {node: i for i, node in enumerate(nodes)}
n = len(nodes)

rows = np.array([node_to_idx[frm] for frm, to in edges], dtype=np.int64)
cols = np.array([node_to_idx[to]  for frm, to in edges], dtype=np.int64)
data = np.ones(len(edges), dtype=np.int64)

A = coo_matrix((data, (rows, cols)), shape=(n, n), dtype=np.int64).tocsr()

# -------------------------------------
# 2. Sum of powers for nilpotent A
#    S = A + A^2 + A^3 + ... until 0
# -------------------------------------
def sum_of_powers_nilpotent(A):
    """
    For a nilpotent sparse matrix A (e.g. adjacency of a DAG),
    compute S = A + A^2 + ... + A^L, where A^{L+1} = 0.

    Returns (S, steps) where steps = L (number of powers added).
    """
    S = csr_matrix(A.shape, dtype=A.dtype)
    Ak = A.copy()
    steps = 0

    # For a DAG with n nodes, longest path <= n-1, so you can set max_steps=n
    max_steps = A.shape[0]

    while Ak.nnz > 0 and steps < max_steps:
        S = S + Ak     # accumulate A^k
        Ak = Ak @ A    # next power
        steps += 1

    return S, steps

S, _ = sum_of_powers_nilpotent(A)

# At this point, S[i,j] = total number of paths of length >=1 from i to j.

def count(u, v):
    return S[node_to_idx[u], node_to_idx[v]]

print( count('you', 'out') )

print( count('svr','dac')*count('dac','fft')*count('fft','out')
     + count('svr','fft')*count('fft','dac')*count('dac','out') )