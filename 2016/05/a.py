import hashlib


def getvalue(input, counter):
  t = input + str(counter)
  return hashlib.md5(t.encode()).hexdigest()

# Part 1
input = 'wtnhxymk'
#input = 'abc'
first_interesting = 10**8

password = ''
for counter in range(10**7):
  output = getvalue(input, counter)
  if output[0:5] == '00000':
    first_interesting = min(counter, first_interesting)
    password += output[5]
    if len(password) == 8:
      break
print(password)

### Part 2
password = list('________')
for counter in range(first_interesting,10**8):
  output = getvalue(input, counter)
  if output[0:5] == '00000':
     pos = int(output[5],16)
     ch = output[6]
     if pos < 8 and password[pos] == '_':
       password[pos] = ch
       print(''.join(password))
       if '_' not in password:
         break
print(''.join(password))
