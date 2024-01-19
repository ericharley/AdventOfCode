def rotate(l, n):
    return l[n:] + l[:n]

lines = open('input.txt').read().strip().split('\n')

def scramble(password):
 for line in lines:
  f = line.split()
  if 'swap position ' in line:
    X = int(f[2])
    Y = int(f[5])
    password[Y],password[X] = password[X],password[Y]

  if 'swap letter ' in line:
    X = password.index(f[2])
    Y = password.index(f[5])
    password[Y],password[X] = password[X],password[Y]

  if 'rotate left ' in line:
    password = rotate(password, int(f[2]))

  if 'rotate right ' in line:
    password = rotate(password, -1*int(f[2]))

  if 'rotate based on position of letter ' in line:
    X = password.index(f[6])
    password = rotate(password, -(1+X))
    if X >= 4:
      password = rotate(password, -1)

  if 'reverse positions ' in line:
    X = int(f[2])
    Y = int(f[4])
    password[X:Y+1] = password[X:Y+1][::-1]

  if 'move position ' in line:
    X = int(f[2])
    Y = int(f[5])
    c = password.pop(X)
    password.insert(Y,c)
 return password  

password = list('abcdefgh')

# Part 1
print(''.join(scramble(password)))

# Part 2

scrambled = list('fbgdceah')
import itertools
for password in itertools.permutations(list('fbgdceah')):
  password = list(password)
  if scramble(password) == scrambled:
    print(''.join(password))
    break
