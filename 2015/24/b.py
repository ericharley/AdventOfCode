import math
import itertools
from operator import mul
from functools import reduce


nums = open('input.txt').read().split('\n')
nums.pop()
nums = [int(n) for n in nums]
T = sum(nums) // 4

min_QE = math.inf
for k in range(1,10):
  for combo in itertools.combinations(nums, k):
    combo = list(combo)
    if sum(combo) == T:
      QE = reduce(mul, combo)
      if QE < min_QE:
        min_QE = QE
        print(reduce(mul, combo), combo)
