lines = open('input.txt').read().strip().split('\n')

total = 0
for line in lines:
   l,w,h = map(int, line.split('x'))
   total += 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)

print(total)


total = 0
for line in lines:
   l,w,h = map(int, line.split('x'))
   total += 2*min(l+w,w+h,h+l) + l*w*h

print(total)
