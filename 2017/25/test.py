from collections import defaultdict

#State,Read,Write,Move,State
A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'

L = -1
R = +1

TM = {
  (A,0):(1,R,B),
  (A,1):(0,L,B),
  (B,0):(1,L,A),
  (B,1):(1,R,A),
}

S = A
N = 6
head = 0
tape = defaultdict(int)

for _ in range(N):
  w,mv,S = TM[S,tape[head]]
  tape[head] = w
  head += mv

print(sum(tape.values()))
