lines = open('input.txt').read().strip().split()

# ships position
x = 0 + 0j
# heading points due east (+x direction)
h = +1

for line in lines:
    d, step = line[0], int(line[1:])
    if d == 'F':
        x = x + step*h
    elif d == 'N':
        x = x + step*(1j)
    elif d == 'S':
        x = x + step*(-1j)
    elif d == 'E':
        x = x + step*(+1)
    elif d == 'W':
        x = x + step*(-1)
    elif d == 'L':
        h = h * (1j ** (step//90))
    elif d == 'R':
        h = h * ((-1j) ** (step//90))
    else:
        print('shouldnt get here')
        
print(int(abs(x.real) + abs(x.imag)))


# ships position
x = 0 + 0j
# waypoint starts 10 units east and 1 unit north
h = 10 + 1j

# Only change here is that the NEWS directions operate on the waypoint not the ship
for line in lines:
    d, step = line[0], int(line[1:])
    if d == 'F':
        x = x + step*h
    elif d == 'N':
        h = h + step*(1j)
    elif d == 'S':
        h = h + step*(-1j)
    elif d == 'E':
        h = h + step*(+1)
    elif d == 'W':
        h = h + step*(-1)
    elif d == 'L':
        h = h * (1j ** (step//90))
    elif d == 'R':
        h = h * ((-1j) ** (step//90))
    else:
        print('shouldnt get here')
        
print(int(abs(x.real) + abs(x.imag)))
