import networkx as nx

grid = open('input.txt').read().splitlines()
board  = {complex(r,c) : int(ch) for r,row in enumerate(grid) for c,ch in enumerate(row) if ch.isdigit()}
groups = {v : [k for k in board if board[k] == v] for v in board.values() }

G = nx.DiGraph( (a,b) for a in board for b in board if abs(a-b) == 1 and (board[b]-board[a] == 1) )

paths = [ list(nx.all_simple_paths(G, start, end)) for start in groups[0] for end in groups[9] ]

print( sum(x>0 for x in map(len, paths)) )

print( sum(map(len, paths)) )
