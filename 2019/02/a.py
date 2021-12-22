with open("input.txt","r") as file:
  v = list(map(int,file.readline().rstrip('\n').split(',')))

#v = [1,9,10,3,2,3,11,0,99,30,40,50]

v[1] = 12
v[2] = 2

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

print(v[0])
