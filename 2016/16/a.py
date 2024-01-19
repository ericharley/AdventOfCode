def getstring(a, n):
  while len(a) < n:
    b = a[::-1]
    b = ''.join(['1' if c == '0' else '0' for c in b])
    a = a + '0' + b
  return a[0:n]

def checksum(a):
  output = ''
  for a,b in zip(a[::2],a[1::2]):
    if a == b:
      output += '1'
    else:
      output += '0'
  if len(output) % 2 == 0:
    return checksum(output)
  else:
    return output

a = getstring('11100010111110100', 272)
print(checksum(a))

a = getstring('11100010111110100', 35651584)
print(checksum(a))

