import re
import string

def is_nice(s):

#  # contains at least three vowels (aeiou only),
#  if sum([1 for ch in s if ch in 'aeiou']) < 3:
#    return False
#
#  # contains at least one letter that appears twice in a row,
#  if sum([1 for x in [ch+ch for ch in string.ascii_lowercase] if x in s]) < 1:
#    return False
#
#  # does not contain the strings ab, cd, pq, or xy
#  if sum([1 for x in [a+b for a,b in zip(s,s[1:])] if x in ['ab', 'cd', 'pq', 'xy']]) > 0:
#    return False

  if re.findall(r'ab|cd|pq|xy', s) or not re.findall(r'(.*[aeiou]){3}', s) or not re.findall(r'(.)\1', s):
    return False

  return True

def is_nice2(s):
  return re.findall(r'(..).*\1', s) and re.findall(r'(.).\1', s)


lines = open('input.txt').read().strip().split('\n')

# Part 1
print(sum([1 for line in lines if is_nice(line)]))

# Part 2
print(sum([1 for line in lines if is_nice2(line)]))
  
