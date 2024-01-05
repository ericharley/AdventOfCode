line = open('input.txt').read().strip()

expanding = False
output = 0

i = 0
while i < len(line):
  ch = line[i]

  if ch != '(' or expanding:
    i += 1
    output += 1

  if ch == '(' and not expanding:
    expanding = True
    i += 1

    a = ''
    while line[i] in '0123456789':
      a = a + line[i]
      i += 1

    if line[i] == 'x':
      i += 1
    else:
      print('Problem! Expected x got a '+line[i]+' , '+line,i)
      exit()

    a = int(a)

    b = ''
    while line[i] in '0123456789':
      b = b + line[i]
      i += 1
    if line[i] == ')':
      i += 1
    else:
      print('Problem! Expected ) got a '+line[i]+' , '+line,i)
      exit()

    b = int(b)

    e = a*b
    output += e
    expanding = False
    i += a

print(output)
