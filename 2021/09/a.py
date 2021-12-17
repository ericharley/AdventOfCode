import numpy as np
from scipy.ndimage import generic_filter
from skimage.segmentation import flood

a = np.genfromtxt("input.txt", dtype=int, delimiter=1)

# Part 1
def test_func(values):
    return np.all(values[2] < values[[0,1,3,4]])

footprint = np.array([[0,1,0],
                      [1,1,1],
                      [0,1,0]])
                      
results = generic_filter(a, test_func, footprint=footprint, mode="constant", cval=10)

print( (a[results == 1] + 1).sum() )

# Part 2
a[a < 9] = 1
basin_coords = np.nonzero(results)
sizes = []
for (x,y) in zip(*basin_coords):
  mask = flood(a, (x,y), tolerance=1, connectivity=1)
  sizes.append(mask.sum())


print(np.prod(sorted(sizes)[-3:]))
