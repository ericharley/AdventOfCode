filename = 'input.txt'

lines = open(filename).read().splitlines()

track = {}
carts = set()

L_TURN = -1j
R_TURN = +1j
ST = +1

UP = -1j
DN = +1j
LT = -1
RT = +1

class Cart:
  def __init__(self, pos: complex, di: complex):
    self.pos = pos
    self.dir = di
    self.next = L_TURN
    self.crashed = False

  def take_turn(self, part):
    if part == '\\':
      self.dir *= {LT:R_TURN, RT:R_TURN, UP:L_TURN, DN:L_TURN}[self.dir]

    elif part == '/':
      self.dir *= {LT:L_TURN, RT:L_TURN, UP:R_TURN, DN:R_TURN}[self.dir]

    elif part == '+':
      self.dir *= self.next
      self.next = {L_TURN:ST,ST:R_TURN,R_TURN:L_TURN}[self.next]

def f(x,y):
  return x + y * 1j

for y,line in enumerate(lines):
  for x,ch in enumerate(line):
    if ch in '<>^v':
      direction = {'^':UP, 'v':DN, '<':LT, '>':RT}[ch]
      carts.add( Cart(f(x,y), direction) )
      ch = {'<':'-','>':'-','v':'|','^':'|'}[ch]

    if ch in "\\/+-|":
      track[f(x,y)] = ch

num_carts = len(carts)

while num_carts > 1:

  cs = sorted(carts, key=lambda c: (c.pos.imag, c.pos.real))

  for cart in cs:
    if not cart.crashed:
      cart.pos += cart.dir
      cart.take_turn(track[cart.pos])

      for otherCart in cs:
        if not otherCart.crashed:
          if cart.pos == otherCart.pos and cart != otherCart:

            print(f'crash at {int(cart.pos.real)},{int(cart.pos.imag)}')

            cart.crashed = True
            otherCart.crashed = True
            num_carts -= 2
            break

# Part 2
for cart in carts:
  if not cart.crashed:
    print(f'cart remains at {int(cart.pos.real)},{int(cart.pos.imag)}')
