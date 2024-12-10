max_score = 0
max_score_2 = 0

i = 0
for a in range(100 + 1):
 for b in range(100 - a + 1):
  for c in range(100 - a - b + 1):
    i += 1
    d = 100 - a - b - c
    capacity = max(0,3*a + -3*b + -1*c)
    durability = max(0,3*b)
    flavor = max(0,4*c + -2*d)
    texture = max(0,-3*a + 2*d)

    score = capacity*durability*flavor*texture
    max_score = max(score, max_score)       

    calories = 2*a+9*b+1*c+8*d
    if calories == 500:
      max_score_2 = max(max_score_2, score)

print(max_score)
print(max_score_2)

