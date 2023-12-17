
filename = 'input.txt'
data = open(filename).read()
lines = [line.split() for line in data.split('\n')]
lines.pop()

hands = {}
for a,b in lines:
    hands[a] = int(b)

card_ranks = {
    'A': 1,
    'K': 2,
    'Q': 3,
#    'J': 4,
    'T': 5,
    '9': 6,
    '8': 7,
    '7': 8,
    '6': 9,
    '5': 10,
    '4': 11,
    '3': 12,
    '2': 13,
    'J': 14,
}

import itertools

def evaluate_hand(hand):
    # Count the frequency of each card
    frequency = {card: hand.count(card) for card in set(hand)}

    # Identify the type of hand based on frequency
    if 5 in frequency.values():
        return 6 # "Five of a kind"
    elif 4 in frequency.values():
        return 5 # "Four of a kind"
    elif sorted(frequency.values()) == [2, 3]:
        return 4 # "Full house"
    elif 3 in frequency.values():
        return 3 # "Three of a kind"
    elif list(frequency.values()).count(2) == 2:
        return 2 # "Two pair"
    elif 2 in frequency.values():
        return 1 # "One pair"
    else:
        return 0 # "High card"

def rep_J(s, chars):
    for p in map(iter, itertools.product(chars, repeat=s.count('J'))):
        yield ''.join(c if c != 'J' else next(p) for c in s)
        
def evaluate_hand_with_J(hand):
    # Count the frequency of each card
    frequency = {card: hand.count(card) for card in set(hand)}
    frequency['J'] = 0
    m = max(frequency, key=lambda key: frequency[key])
    return evaluate_hand(''.join([c if c != 'J' else m for c in hand]))
    
def order_hands_with_J(a, b):
    if evaluate_hand_with_J(a) == evaluate_hand_with_J(b):
        for i in range(len(a)):
            if card_ranks[a[i]] < card_ranks[b[i]]:
                return 1
            elif card_ranks[a[i]] > card_ranks[b[i]]:
                return -1
        return 0
    
    else:
        if evaluate_hand_with_J(a) < evaluate_hand_with_J(b):
            return -1
        else:
            return 1
        
from functools import cmp_to_key
order_hands_with_J_key = cmp_to_key(order_hands_with_J)

scores = list(zip(range(1,len(hands)+1), sorted(hands.keys(), key=order_hands_with_J_key)))

t = 0
for rank, hand in scores:
    t += rank*hands[hand]
print(t)
