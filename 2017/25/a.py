from collections import defaultdict

#State,Read,Write,Move,State
L,R = -1, +1

TM = {
  ('A',0):(1,R,'B'),
  ('A',1):(0,R,'C'),
  ('B',0):(0,L,'A'),
  ('B',1):(0,R,'D'),
  ('C',0):(1,R,'D'),
  ('C',1):(1,R,'A'),
  ('D',0):(1,L,'E'),
  ('D',1):(0,L,'D'),
  ('E',0):(1,R,'F'),
  ('E',1):(1,L,'B'),
  ('F',0):(1,R,'A'),
  ('F',1):(1,R,'E'),
}

S = 'A'
N = 12368930
head = 0
tape = defaultdict(int)

for _ in range(N):
  w,mv,S = TM[S,tape[head]]
  tape[head] = w
  head += mv

print(sum(tape.values()))
