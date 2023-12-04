import sys

# Parsing the game data and determining which games are possible with the given cube configuration
def parse_game_data(game_data):
    # Parsing each game's data and returning a dictionary with game ID and cube counts
    games = {}
    for line in game_data.strip().split('\n'):
        parts = line.split(': ')
        game_id = int(parts[0].split(' ')[1])
        rounds = parts[1].split('; ')
        games[game_id] = []
        for round in rounds:
            cube_counts = {'red':0,'blue':0,'green':0}
            for cube_info in round.split(', '):
                count, color = cube_info.split(' ')
                cube_counts[color] = int(count)
            games[game_id].append(cube_counts)
    return games

def is_game_possible(game, max_cubes):
    # Checking if a game is possible given the maximum cubes of each color
    for round in game:
        for color, count in round.items():
            if count > max_cubes[color]:
                return False
    return True

# Parse the game data
games_data = open(sys.argv[1]).read().strip()
games = parse_game_data(games_data)

# Part 1
# Determine which games are possible and calculate the sum of their IDs
# Maximum number of each color of cubes in the bag
max_cubes = {'red': 12, 'green': 13, 'blue': 14}
possible_games_sum = sum( game_id for game_id, rounds in games.items() if is_game_possible(rounds, max_cubes) )

print(possible_games_sum)

#Part 2
from functools import reduce
from operator import mul
a = [([max([x[y] for x in z]) for y in ['red','blue','green']]) for z in games.values()]
v = sum(reduce(mul, l, 1) for l in a)
print(v)

