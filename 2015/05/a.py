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

  return bool(not re.findall(r'ab|cd|pq|xy', s) and re.findall(r'(.*[aeiou]){3}', s) and re.findall(r'(.)\1', s))

def is_nice2(s):
  return bool(re.findall(r'(..).*\1', s) and re.findall(r'(.).\1', s))


inp = open('input.txt').readlines()

# Part 1
print(sum(is_nice(x) for x in inp))

# Part 2
print(sum(is_nice2(x) for x in inp))
  
