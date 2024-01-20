x = list(map(int, open('input.txt').read().strip()))
n = len(x)

t = sum([x[i] for i in range(n) if x[i] == x[(i+1) % n]])
print(t)

r = n//2
t = sum([x[i] for i in range(n) if x[i] == x[(i+r) % n]])
print(t)
