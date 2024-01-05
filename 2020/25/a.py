## Discrete log with baby step / giant step
#
def bsgs(α, β, p):
  '''
  Find x such that β = α^x mod p, p prime.
  '''
  from math import ceil, sqrt

  m = ceil(sqrt(p))
  table = { pow(α, j, p) : j for j in range(m) }

  α_inv_m = pow(α, -m, p)
  γ = β
  for i in range(m):
    if γ in table:
      return i*m + table[γ]
    γ = (γ * α_inv_m) % p

## Read input
card_pk, door_pk = map(int, open('input.txt').read().strip().split('\n'))
p = 20201227
subject_number = 7

## Brute Force
#for i in range(10000000):
#  if door_pk == pow(subject_number, i, p):
#    door_loop = i
#    break
#
#print(pow(card_pk, door_loop, p))
#
#for i in range(100000000):
#  if card_pk == pow(subject_number, i, p):
#    card_loop = i
#    break
#
#print(pow(door_pk, card_loop, p))

card_loop = bsgs(subject_number, card_pk, p) 
print(pow(door_pk, card_loop, p))

# These should be equal
#print(pow(card_pk, door_loop, p))
#door_loop = bsgs(subject_number, door_pk, p)

