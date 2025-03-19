from collections import Counter

# Define card values for ranking
CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
               '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def get_hand_rank(cards):
    """Determine the rank of the poker hand."""
    values = sorted([CARD_VALUES[card[0]] for card in cards], reverse=True)
    suits = [card[1] for card in cards]
    
    value_counts = Counter(values)
    counts = sorted(value_counts.values(), reverse=True)
    is_flush = len(set(suits)) == 1
    is_straight = values == list(range(values[0], values[0] - 5, -1))

    # Determine hand ranking
    if is_flush and is_straight:
        return (9, values)  # Straight Flush
    elif 4 in counts:
        return (8, sorted(value_counts, key=lambda x: (value_counts[x], x), reverse=True))  # Four of a Kind
    elif counts == [3, 2]:
        return (7, sorted(value_counts, key=lambda x: (value_counts[x], x), reverse=True))  # Full House
    elif is_flush:
        return (6, values)  # Flush
    elif is_straight:
        return (5, values)  # Straight
    elif 3 in counts:
        return (4, sorted(value_counts, key=lambda x: (value_counts[x], x), reverse=True))  # Three of a Kind
    elif counts == [2, 2, 1]:
        return (3, sorted(value_counts, key=lambda x: (value_counts[x], x), reverse=True))  # Two Pair
    elif 2 in counts:
        return (2, sorted(value_counts, key=lambda x: (value_counts[x], x), reverse=True))  # One Pair
    else:
        return (1, values)  # High Card

def compare_hands(hand1, hand2):
    """Compare two hands and determine the winner."""
    rank1, values1 = get_hand_rank(hand1)
    rank2, values2 = get_hand_rank(hand2)

    if rank1 > rank2:
        return 1  # Player 1 wins
    elif rank1 < rank2:
        return 2  # Player 2 wins
    else:
        return 1 if values1 > values2 else 2

def count_player1_wins(hands):
    """Count the number of hands won by Player 1."""
    player1_wins = 0
    for hand in hands:
        player1 = hand[:5]
        player2 = hand[5:]
        if compare_hands(player1, player2) == 1:
            player1_wins += 1
    return player1_wins

# Read input
n = int(input().strip())
hands = [input().strip().split() for _ in range(n)]

# Compute and print the number of wins for Player 1
print(count_player1_wins(hands))
