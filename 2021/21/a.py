# INPUT
# Player 1 starting position: 7
# Player 2 starting position: 9

dice_rolls = [(x % 100) + 1 for x in list(range(10001))]

p1_pos = 7
p1_score = 0

p2_pos = 9
p2_score = 0

i = 0
while True:
  roll = sum(dice_rolls[i:i+3])
  i += 3
  p1_pos = ((p1_pos+roll-1) % 10) + 1
  p1_score += p1_pos

  if p1_score >= 1000:
    break

  roll = sum(dice_rolls[i:i+3])
  i += 3
  p2_pos = ((p2_pos+roll-1) % 10) + 1
  p2_score += p2_pos

  if p2_score >= 1000:
    break


v = min(p1_score, p2_score) * i
print(v)
