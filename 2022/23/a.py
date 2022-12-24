elves = set()

#for r, line in enumerate(open("test.txt")):
for r, line in enumerate(open("input.txt")):
    for c, item in enumerate(line[:-1]):
        if item == "#":
            elves.add(c + r * 1j)

# print(elves)

def print_grid():
 for r in range(12):
  for c in range(14):
   if (c + r*1j) in elves:
     print('#',end='')
   else:
     print('.',end='')
  print()

#print('== Initial State ==')
#print_grid()
#input()

neighborhood = [-1-1j, -1j, 1-1j, -1, +1, -1+1j, +1j, 1+1j]

moves = [-1j, +1j, -1, +1]

scanmap = {
    -1j: [-1j - 1, -1j, -1j + 1],
     1j: [ 1j - 1,  1j,  1j + 1],
      1: [ 1 - 1j,  1,    1 + 1j],
     -1: [-1 - 1j, -1, -  1 + 1j]
}

# do one round
for round in range(10):
 proposed = {}
 for elf in elves:
   # check neighborhood for elves 
   if not any(elf + x in elves for x in neighborhood):
     continue
 
   # propose a move for this elf
   for move in moves:
     # if all the slots are empty for this move then we can propose moving there
     if all((elf + m) not in elves for m in scanmap[move]):
         if (elf+move) in proposed:
           proposed[elf+move].append(elf)
         else:
           proposed[elf + move] = [elf]
         break
 
 for new_loc in proposed:
   if len(proposed[new_loc]) == 1:
     elves.remove(proposed[new_loc][0])
     elves.add(new_loc)
 
 ## cycle the moves list
 moves.append(moves.pop(0))

 #print(f'== End of Round {round+1} ==')
 #print_grid()
 #input()

# all elves have proposed moves
# for all the proposed moves, if only one was proposed...

# c := x position
# r := y position

# -1-1j  0-1j  +1-1j
# -1-0j  0-0j  +1-0j
# -1+1j  0+1j  +1+1j


mx = min(x.real for x in elves)
Mx = max(x.real for x in elves)
my = min(x.imag for x in elves)
My = max(x.imag for x in elves)

print((Mx - mx + 1) * (My - my + 1) - len(elves))
