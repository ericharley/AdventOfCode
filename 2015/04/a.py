import hashlib

def getvalue(input, counter):
  t = input + str(counter)
  return hashlib.md5(t.encode()).hexdigest()


# Part 1
input = 'yzbqklnj'
for counter in range(10**7):
  output = getvalue(input, counter)
  if output[0:5] == '00000':
    print(counter)
    break

## Part 2
input = 'yzbqklnj'
for counter in range(10**7):
  output = getvalue(input, counter)
  if output[0:6] == '000000':
    print(counter)
    break

