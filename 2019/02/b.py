import itertools

noun = 0
verb = 0

with open("input.txt","r") as file:
  ov = list(map(int,file.readline().rstrip('\n').split(',')))

#v = [1,9,10,3,2,3,11,0,99,30,40,50]


for noun,verb in itertools.product(range(100),range(100)):
  v = ov.copy()
  v[1] = noun
  v[2] = verb

  ip = 0
  while True:
    # print(ip, v)
    op = v[ip]

    if op == 99:
      # halt
      break

    elif op == 1:
      # add   
      loc1 = v[ip+1]
      loc2 = v[ip+2]
      loc3 = v[ip+3]
      v[loc3] = v[loc1] + v[loc2]
      ip += 4

    elif op == 2:
      # multiply
      loc1 = v[ip+1]
      loc2 = v[ip+2]
      loc3 = v[ip+3]
      v[loc3] = v[loc1] * v[loc2]
      ip += 4

    else:
      #error
      print('ERROR unknown op code', op)
      exit()

  if v[0] == 19690720:
    break

print(v[0])
print(100 * noun + verb)
