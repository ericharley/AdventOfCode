import re

def incCh(c):
 if c == 'z':
    return 'a'
 else:
    return chr(ord(c) + 1)

def incStr(s):
 if s:
   c, r = s[0], s[1:]
   nxt = incCh(c)
   if c == 'z':
     return nxt + incStr(r)
   else:
     return nxt + r
 else :
   return ''

def f(a):
  b = incCh(a)
  c = incCh(b)
  return a+b+c

rr = re.compile( '|'.join([f(a) for a in 'abcdefghijklmnopqrstuvwx']) )

def valid(s):
  # increasing straight of three letters, abc, bcd, cde, ...
  if not rr.search(s):
    return False

  # no i, o, or l
  if re.search(r'i|o|l', s):
    return False

  # contain at least two different, non-overlapping pairs of letters
  # like xxyzz
  matches = re.findall(r'(.)\1', s)
  if len(matches) < 2:
    return False

  return True

def doit(s):
  # reverse it
  r = s[::-1]
  for i in range(1324555+1):
    r = incStr(r)
    if valid(r[::-1]):
      print(r[::-1])

doit('hepxcrrq')
