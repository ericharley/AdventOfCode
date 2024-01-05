line = open('input.txt').read().strip()

def decompress(s):

  # nothing to decompress, so just return length
  if '(' not in s:
    return len(s)

  # otherwise
  ret = 0
  # while there is stuff to decompress
  while '(' in s:
    # jump to the next marker
    idx = s.find('(') 
    ret += idx
    s = s[idx:]
    # parse marker
    A,B = map(int, s[1:s.find(')')].split('x'))
    # advance pointer past marker
    s = s[s.find(')')+1:]

    # recursively decompress the marker and then replicate
    ret += decompress(s[:A])*B

    # advance past the repetitions
    s = s[A:]

  # we're done, so get the remaining characters
  ret += len(s)
  return ret
    

print(decompress(line))
