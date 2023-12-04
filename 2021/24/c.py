w = [0,1,3,5,7,9,2,4,6,8,9,9,9,9,9]

def doit(w):
	x = 0
	y = 0
	z = 0

	# inp w
	x = 0
	x = x + z
	x = x % 26
	#z = z // 1
	x = x + 12
	#x = int(x == w)
	#x = int(x == 0)
	if x == w[1]:
	 x = 0
	else:
	 x = 1

	y = 0
	y = y + 25
	y = y * x
	y = y + 1
	z = z * y
	y = 0
	y = y + w[1]
	y = y + 4
	y = y * x
	z = z + y

	# inp w
	x = 0
	x = x + z
	x = x % 26
	#z = z // 1
	x = x + 11
	#x = int(x == w)
	#x = int(x == 0)
	if x == w[2]:
	 x = 0
	else:
	 x = 1

	y = 0
	y = y + 25
	y = y * x
	y = y + 1
	z = z * y
	y = 0
	y = y + w[2]
	y = y + 10
	y = y * x
	z = z + y

	# inp w
	x = 0
	x = x + z
	x = x % 26
	#z = z // 1
	x = x + 14
	#x = int(x == w)
	#x = int(x == 0)
	if x == w[3]:
	 x = 0
	else:
	 x = 1

	y = 0
	y = y + 25
	y = y * x
	y = y + 1
	z = z * y
	y = 0
	y = y + w[3]
	y = y + 12
	y = y * x
	z = z + y

	# inp w
	x = 0
	x = x + z
	x = x % 26
	z = z // 26
	x = x + -6
	#x = int(x == w)
	#x = int(x == 0)
	if x == w[4]:
	 x = 0
	else:
	 x = 1

	y = 0
	y = y + 25
	y = y * x
	y = y + 1
	z = z * y
	y = 0
	y = y + w[4]
	y = y + 14
	y = y * x
	z = z + y

	# inp w
	x = 0
	x = x + z
	x = x % 26
	#z = z // 1
	x = x + 15
	#x = int(x == w)
	#x = int(x == 0)
	if x == w[5]:
	 x = 0
	else:
	 x = 1

	y = 0
	y = y + 25
	y = y * x
	y = y + 1
	z = z * y
	y = 0
	y = y + w[5]
	y = y + 6
	y = y * x
	z = z + y


	###

	# inp w
	x = 0
	x = x + z
	x = x % 26
	#z = z // 1
	x = x + 12
	#x = int(x == w)
	#x = int(x == 0)
	if x == w[6]:
	 x = 0
	else:
	 x = 1

	y = 0
	y = y + 25
	y = y * x
	y = y + 1
	z = z * y
	y = 0
	y = y + w[6]
	y = y + 16
	y = y * x
	z = z + y

	# inp w
	x = 0
	x = x + z
	x = x % 26
	z = z // 26
	x = x + -9
	#x = int(x == w)
	#x = int(x == 0)
	if x == w[7]:
	 x = 0
	else:
	 x = 1

	y = 0
	y = y + 25
	y = y * x
	y = y + 1
	z = z * y
	y = 0
	y = y + w[7]
	y = y + 1
	y = y * x
	z = z + y

	# inp w
	x = 0
	x = x + z
	x = x % 26
	#z = z // 1
	x = x + 14
	#x = int(x == w)
	#x = int(x == 0)
	if x == w[8]:
	 x = 0
	else:
	 x = 1

	y = 0
	y = y + 25
	y = y * x
	y = y + 1
	z = z * y
	y = 0
	y = y + w[8]
	y = y + 7
	y = y * x
	z = z + y

	# inp w
	x = 0
	x = x + z
	x = x % 26
	#z = z // 1
	x = x + 14
	#x = int(x == w)
	#x = int(x == 0)
	if x == w[9]:
	 x = 0
	else:
	 x = 1

	y = 0
	y = y + 25
	y = y * x
	y = y + 1
	z = z * y
	y = 0
	y = y + w[9]
	y = y + 8
	y = y * x
	z = z + y

	# inp w
	x = 0
	x = x + z
	x = x % 26
	z = z // 26
	x = x + -5
	#x = int(x == w)
	#x = int(x == 0)
	if x == w[10]:
	 x = 0
	else:
	 x = 1

	y = 0
	y = y + 25
	y = y * x
	y = y + 1
	z = z * y
	y = 0
	y = y + w[10]
	y = y + 11
	y = y * x
	z = z + y

	# inp w
	x = 0
	x = x + z
	x = x % 26
	z = z // 26
	x = x + -9
	#x = int(x == w)
	#x = int(x == 0)
	if x == w[11]:
	 x = 0
	else:
	 x = 1

	y = 0
	y = y + 25
	y = y * x
	y = y + 1
	z = z * y
	y = 0
	y = y + w[11]
	y = y + 8
	y = y * x
	z = z + y

	# inp w
	x = 0
	x = x + z
	x = x % 26
	z = z // 26
	x = x + -5
	#x = int(x == w)
	#x = int(x == 0)
	if x == w[12]:
	 x = 0
	else:
	 x = 1

	y = 0
	y = y + 25
	y = y * x
	y = y + 1
	z = z * y
	y = 0
	y = y + w[12]
	y = y + 3
	y = y * x
	z = z + y

	# inp w
	x = 0
	x = x + z
	x = x % 26
	z = z // 26
	x = x + -2
	#x = int(x == w)
	#x = int(x == 0)
	if x == w[13]:
	 x = 0
	else:
	 x = 1

	y = 0
	y = y + 25
	y = y * x
	y = y + 1
	z = z * y
	y = 0
	y = y + w[13]
	y = y + 1
	y = y * x
	z = z + y

	# inp w
	x = 0
	x = x + z
	x = x % 26
	z = z // 26
	x = x + -7
	#x = int(x == w)
	#x = int(x == 0)
	if x == w[14]:
	 x = 0
	else:
	 x = 1

	y = 0
	y = y + 25
	y = y * x
	y = y + 1
	z = z * y
	y = 0
	y = y + w[14]
	y = y + 8
	y = y * x
	z = z + y
	
	return z
	
#    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
#w = [0,9,1,3,9,7,2,9,9,3,6,7,8,9,6]
w = [0,9,1,3,9,8,2,9,9,6,9,7,9,9,6]
#    0,9 1 3 9 8 2 9 9 6 9 7 9 9 6 
#for a in range(1,10):
#  w[14] = a
#  print(doit(w),a)
print(doit(w)) 
