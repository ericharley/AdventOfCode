lines = open('input.txt').read().splitlines()

data = []
for line in lines:
  a, *ns = list(map(int,line.replace(':','').split(' ')))
  data += [(a,ns)]

def g(target, nums, part2 = False):
  if len(nums) == 1:
    return target == nums[0]

  # +
  if target >= nums[-1] and g(target - nums[-1], nums[:-1], part2):
    return True

  # *
  if target % nums[-1] == 0 and g(target // nums[-1], nums[:-1], part2):
    return True

  # ||
  if part2:
    target, num = str(target), str(nums[-1])
    if target.endswith(num) and target != num:
      return g(int(target[:-len(num)]), nums[:-1], part2)

# Part 1
print( sum([a for a,ns in data if g(a,ns)]) )

# Part 2
print( sum([a for a,ns in data if g(a,ns, part2=True)]) )

