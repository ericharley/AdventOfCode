# Parameter Modes
#
# 0 : position , parameter to be interpreted as a position
# 1 : immediate, parameter is interpreted as a value
#
#
#ABCDE
# 1002
#
#DE - two-digit opcode,      02 == opcode 2
# C - mode of 1st parameter,  0 == position mode
# B - mode of 2nd parameter,  1 == immediate mode
# A - mode of 3rd parameter,  0 == position mode,
#                                  omitted due to being a leading zero
#
def decode_op(val):
  s  = '0' * (5-len(str(val))) + str(val)
  DE = int(s[3:5])
  C  = int(s[2:3])
  B  = int(s[1:2])
  A  = int(s[0:1])
  return(DE,C,B,A)

def get_input():
  return 5

def put_output(x):
  print('OUTPUT', x)
  return

with open("input.txt","r") as file:
  ov = list(map(int,file.readline().rstrip('\n').split(',')))

#v = [1002,4,3,4,33]
#v = [1101,100,-1,4,0]
v = ov.copy()
#v = [3,9,8,9,10,9,4,9,99,-1,8 ]
#v = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
#v = [3,9,8,9,10,9,4,9,99,-1,8]
#v = [3,3,1108,-1,8,3,4,3,99]
if True:
  ip = 0
  while True:
    (op,M1,M2,M3) = decode_op(v[ip])
#    print(ip, (op,M1,M2,M3))
    if op == 99:
      # halt
      break

    elif op == 1:
      # add
      loc1 = v[ip+1]
      loc2 = v[ip+2]
      loc3 = v[ip+3]
      a = v[loc1] if M1 == 0 else loc1
      b = v[loc2] if M2 == 0 else loc2
      v[loc3] = a + b
      ip += 4

    elif op == 2:
      # multiply
      loc1 = v[ip+1]
      loc2 = v[ip+2]
      loc3 = v[ip+3]
      a = v[loc1] if M1 == 0 else loc1
      b = v[loc2] if M2 == 0 else loc2
      v[loc3] = a * b
      ip += 4

    elif op == 3:
      # input
      loc1 = v[ip+1]
      v[loc1] = get_input()
      ip += 2

    elif op == 4:
      # output
      loc1 = v[ip+1]
      put_output((v[loc1] if M1 == 0 else loc1))
      ip += 2

    elif op == 5:
      # jump-if-true if the first parameter is non-zero, it sets the 
      # instruction pointer to the value from the second parameter. 
      # Otherwise, it does nothing.
      loc1 = v[ip+1]
      loc2 = v[ip+2]
      a = v[loc1] if M1 == 0 else loc1
      b = v[loc2] if M2 == 0 else loc2
      if a != 0:
        ip = b
      else:
        ip += 3

    elif op == 6:
      # jump-if-false if the first parameter is zero, it sets the 
      # instruction pointer to the value from the second parameter. 
      # Otherwise, it does nothing.
      loc1 = v[ip+1]
      loc2 = v[ip+2]
      a = v[loc1] if M1 == 0 else loc1
      b = v[loc2] if M2 == 0 else loc2
      if a == 0:
        ip = b
      else:
        ip += 3

    elif op == 7:
      # less than if the first parameter is less than the second 
      # parameter, it stores 1 in the position given by the third 
      # parameter. Otherwise, it stores 0.
      loc1 = v[ip+1]
      loc2 = v[ip+2]
      loc3 = v[ip+3]
      a = v[loc1] if M1 == 0 else loc1
      b = v[loc2] if M2 == 0 else loc2
      v[loc3] = 1 if a < b else 0
      ip += 4

    elif op == 8:
      # equals if the first parameter is equal to the second parameter, 
      # it stores 1 in the position given by the third parameter. 
      # Otherwise, it stores 0.
      loc1 = v[ip+1]
      loc2 = v[ip+2]
      loc3 = v[ip+3]
      a = v[loc1] if M1 == 0 else loc1
      b = v[loc2] if M2 == 0 else loc2
      v[loc3] = 1 if a == b else 0
      ip += 4

    else:
      #error
      print('ERROR unknown op code', op)
      exit()
