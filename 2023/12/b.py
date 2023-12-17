import re
data = open("input.txt").read().splitlines()

cache = {}

def count(config, nums):
  key = (config, nums)
  if key in cache:
    return cache[key]

  # base cases
  # if the configuration is empty, and we have no runs to place, otherwise...
  if config == '' and nums == ():
    return 1
  if config == '' and nums != ():
    return 0

  # if there are no more runs to place
  if nums == () and not '#' in config:
    return 1
  if nums == () and '#' in config:
    return 0

  curr_ch = config[0]
  k = nums[0]

  result = 0
  # a run either starts here or it doesn't 
  # starts here
  if curr_ch == '#' or curr_ch == '?':
    # if we can start a run here
    #  there's a run of k #'s and ?s, and the ending character is . or ? or end of string
    if re.match(r'^[#?]{'+str(k)+r'}([.?]|$)', config):
      result += count(config[(k+1):], nums[1:])

  # doesn't start here
  if curr_ch == '.' or curr_ch == '?':
    result += count(config[1:], nums)

  cache[key] = result
  return result



total = 0
for line in data:
    config, nums = line.split()
    nums = tuple(map(int, nums.split(",")))
    total += count(config, nums)

print(total)


total = 0
for line in data:
    config, nums = line.split()
    nums = tuple(map(int, nums.split(",")))
    
    config = "?".join([config] * 5)
    nums *= 5
    
    total += count(config, nums)

print(total)

