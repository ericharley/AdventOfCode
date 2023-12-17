from functools import lru_cache

@lru_cache(maxsize=99999)
def count(config, nums):

  # base cases
  # string is empty, and no more numbers to place
  if config == '' and nums == ():
    return 1
  # ... or there's more to place
  if config == '' and nums != ():
    return 0

  # no more numbers to place and nothing placed left
  if nums == () and not '#' in config:
    return 1
  # ... or there is something left to place...
  if nums == () and '#' in config:
    return 0
  
  # otherwise
  ch = config[0]
  k = nums[0]
  rest = nums[1:]

  result = 0
  
  # we either start a run here or not
  # 
  # don't start a run here
  if ch in '.?':
    result += count(config[1:], nums)

  # start a run here
  if ch in '#?':
    # we can do this if there's a length k block of #/? 
      if k <= len(config) and (not '.' in config[:k]) and (len(config) == k or config[k] != '#'):
        result += count(config[(k+1):], rest) # place a length k block of # and a single .

  return result

total = 0 
for line in open("input.txt").read().splitlines():
    config, nums = line.split()
    nums = tuple(map(int, nums.split(",")))

    total += count(config, nums)
    
print(total)

total = 0 
for line in open("input.txt").read().splitlines():
    config, nums = line.split()
    nums = tuple(map(int, nums.split(",")))

    config = '?'.join([config]*5)
    nums *= 5
    total += count(config, nums)
    
print(total)


