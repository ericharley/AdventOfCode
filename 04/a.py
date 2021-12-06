import numpy as np

def board_is_a_winner(draws, board):
   n = 5
   draws = set(draws)
   for i in range(n):
     row = set(board[i,:])
     col = set(board[:,i])
     if ( len(row.intersection(draws)) == 5 ):
        return True, board[i,:]
     if ( len(col.intersection(draws)) == 5 ):
        return True, board[:,i]
   return False, []

def score_board(draws, board):
   mask = np.isin(board, draws)
   v = np.sum(board[~mask]) * draws[-1]
   return v


# read the input
# file = open("test.txt","r")
file = open("input.txt","r")

draws = file.readline().rstrip('\n')
draws = [int(i) for i in draws.split(',')]

boards = []
while True:
  line = file.readline()
  if not line:
        break
  board = np.zeros((5,5),dtype=int)
  for i in range(5):
     line = list(filter(lambda x: x, file.readline().rstrip('\n').split(' ')))
     line = [int(x) for x in line]
     board[i,:] = line
  boards.append(board)

x = False
for i in range(1,len(draws)+1):
   if x : break
   for board in boards:
      (x,_) = board_is_a_winner(draws[0:i], board)
      if x : 
        print(score_board(draws[0:i], board))
        break

d = {}
for (j, board) in zip(range(len(boards)), boards):
  for i in range(1,len(draws)+1):
    (x,_) = board_is_a_winner(draws[0:i], board)
    if x:
       d[j] = i
       break;

last_board = max(d, key=d.get)
print(score_board(draws[0:d[last_board]], boards[last_board]))
