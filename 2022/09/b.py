# Number of knots
k = 10
v = set([(0, 0)])

H = [0, 0]
T = [0, 0]

R = [[0, 0] for _ in range(k)]

for line in open(0):
    x, y = line.split()
    y = int(y)

    dx = 1 if x == "R" else (-1 if x == "L" else 0)
    dy = 1 if x == "U" else (-1 if x == "D" else 0)

    for _ in range(y):

      R[0][0] += dx   # new H
      R[0][1] += dy

      # for each knot, the head is this knot, and the tail is the next knot
      for i in range(k-1):
        H = R[i]
        T = R[i+1]

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
        

      # R[-1] is the last knot
      v.add(tuple(R[-1]))

print(len(v))
