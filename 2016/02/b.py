# Keypad
#
#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D

# F
# R
# O   TO
# M
#    UDLR
m = {
'1':'1311',
'2':'2623',
'3':'1724',
'4':'4834',
'5':'5556',
'6':'2A57',
'7':'3B68',
'8':'4C79',
'9':'9989',
'A':'6AAB',
'B':'7DAC',
'C':'8CBC',
'D':'BDDD'
}

c = '5'
lines = open('input.txt').read().strip().split('\n')
for line in lines:
  for op in line:
    c = m[c]['UDLR'.find(op)]
  print(c,end='')
print()
