v = set([(0, 0)])

H = [0, 0]
T = [0, 0]

#def print_grid():
#  for c in range(0,5,1):
#    for r in range(0,5,1):
#      if r == H[0] and c == H[1]:
#        print('H', end='')
#      elif r == T[0] and c == T[1]:
#        print('T', end='')
#      else:
#        print('.', end='')
#    print()
#  print()

for line in open(0):
    x, y = line.split()
    y = int(y)

    dx = 1 if x == "R" else (-1 if x == "L" else 0)
    dy = 1 if x == "U" else (-1 if x == "D" else 0)
#    print(x,y,dx,dy)

    for _ in range(y):

      H[0] += dx
      H[1] += dy

      # If the head is ever two steps directly up, down, left, or right
      # from the tail, the tail must also move one step in that
      # direction so it remains close enough
      Δx = H[0] - T[0]
      Δy = H[1] - T[1]
      if abs(Δx) == 2 or abs(Δy) == 2:
        if Δx == 0:
          T[1] += +1 if Δy > 0 else -1
        elif Δy == 0:
          T[0] += +1 if Δx > 0 else -1
        else:
          T[0] += 1 if Δx > 0 else -1
          T[1] += 1 if Δy > 0 else -1
        

      v.add(tuple(T))
#      print(H)

#    print_grid()
    #  Δx = 1
    #  Δy = 1

print(len(v))
