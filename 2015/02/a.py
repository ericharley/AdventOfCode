lines = open('input.txt').readlines()

# Part 1
total = 0
for line in lines:
   l,w,h = map(int, line.split('x'))
   total += 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)

print(total)


# Part 2
total = 0
for line in lines:
   l,w,h = map(int, line.split('x'))
   total += 2*min(l+w,w+h,h+l) + l*w*h

print(total)
