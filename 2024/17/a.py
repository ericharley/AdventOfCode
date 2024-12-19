def f(a):
 ip = 0
 #a = 37293246
 #a = 117440
 b = 0
 c = 0

 def get_combo_operand(v):
  if 0 <= v <= 3:
    return v

  if v == 4:
    return a

  if v == 5:
    return b

  if v == 6:
    return c



 program = [2,4,1,6,7,5,4,4,1,7,0,3,5,5,3,0]
 #program = [0,3,5,4,3,0]
 output = []

 while 0 <= ip < len(program):
  
  instruction,operand = program[ip],program[ip+1]
  combo_operand = get_combo_operand(operand)
  literal_operand = operand

  if instruction == 0:  # adv
    numerator = a
    denominator = 2**combo_operand
    a = (numerator // denominator)

  if instruction == 1:  # bxl
    b = b ^ literal_operand

  if instruction == 2:  # bst
    b = combo_operand % 8

  if instruction == 3:  # jnz
    if a != 0:
      ip = literal_operand
      continue

  if instruction == 4:  # bxc
    b = b ^ c

  if instruction == 5:  # out
    v = combo_operand % 8
    output.append(v)

  if instruction == 6:  # bdv
    numerator = a
    denominator = 2**combo_operand  
    b = (numerator // denominator)

  if instruction == 7:  # cdv
    numerator = a
    denominator = 2**combo_operand  
    c = (numerator // denominator)

  ip += 2

 #print(output)
 #print(all(x == y for x,y in zip(output,program)))
 if len(output)==len(program):
   return all(x == y for x,y in zip(output,program))
 return False

for a in range(1,2*10**8):
  if f(a):
    print(a)
    break
