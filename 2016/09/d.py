line = open('input.txt').read().strip()

def decompress(s):

  # nothing to decompress, so just return length
  if '(' not in s:
    return len(s)

  # there's a first marker, find it and parse it
  left_idx = s.find('(')
  right_idx = s.find(')')
  A, B = map(int, s[left_idx+1:right_idx].split('x'))

  #
  # string has three parts:
  #
  # 1. part up to the marker
  #
  #  s[:left_idx]
  #
  # 2. the marker
  #
  #  s[left_idx:right_idx+1]
  #
  # 2a. stuff covered by the marker
  #
  #  s[right_idx+1:right_idx+1+A]
  #
  #    don't decompress it, just copy it B times
  #    it's contribution to expanded length is A * B
  #
  # 3. process the stuff after the marker
  #
  #  s[right_idx+1+A:]
  #

  return left_idx + A*B + decompress(s[right_idx+1+A:])

print(decompress(line))


def decompress(s):

  # nothing to decompress, so just return length
  if '(' not in s:
    return len(s)

  # there's a first marker, find it and parse it
  left_idx = s.find('(')
  right_idx = s.find(')')
  A, B = map(int, s[left_idx+1:right_idx].split('x'))

  #
  # string has three parts:
  #
  # 1. part up to the marker
  #
  #  s[:left_idx]
  #
  # 2. the marker
  #
  #  s[left_idx:right_idx+1]
  #
  # 2a. stuff covered by the marker
  #
  #  s[right_idx+1:right_idx+1+A]
  #
  #    decompress it, copy it B times
  #    it's contribution to expanded length is B * result of recursive call to decompress()
  #
  # 3. process the stuff after the marker
  #
  #  s[right_idx+1+A:]

  return left_idx + B*decompress(s[right_idx+1:right_idx+1+A]) + decompress(s[right_idx+1+A:])

print(decompress(line))
