s = open('input.txt').read()
r,c = list(map(int,''.join([ch for ch in s if (ch.isdigit() or ch == ' ')]).split()))

def g(r,c):
  return c*(c + 1)//2 + r*(r-1)//2 + (r-1)*(c-1)

N = g(r,c)

# Slow
prev_code = 20151125
for i in range(N-1):
  prev_code = 252533*prev_code % 33554393
print(prev_code)

# Fast
x0  = 20151125
exp = g(r,c)-1
mod = 33554393
xn  = pow(252533, exp, mod) * 20151125 % mod

print(xn)
