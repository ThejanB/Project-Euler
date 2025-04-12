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
    unique_values = sorted(value_counts.keys(), reverse=True)
    
    is_flush = len(set(suits)) == 1
    is_straight = len(unique_values) == 5 and (unique_values[0] - unique_values[-1] == 4)
    
    # Handle Ace-low straight (A, 2, 3, 4, 5)
    if set(values) == {14, 2, 3, 4, 5}:  
        is_straight = True
        values = [5, 4, 3, 2, 1]  # Lowest high card in case of tiebreak

    # Determine hand ranking
    if is_flush and is_straight:
        return (9, values)  # Straight Flush
    elif 4 in counts:
        return (8, [k for k, v in value_counts.items() if v == 4] + [k for k, v in value_counts.items() if v == 1])  # Four of a Kind
    elif counts == [3, 2]:
        return (7, [k for k, v in value_counts.items() if v == 3] + [k for k, v in value_counts.items() if v == 2])  # Full House
    elif is_flush:
        return (6, values)  # Flush
    elif is_straight:
        return (5, values)  # Straight
    elif 3 in counts:
        return (4, [k for k, v in value_counts.items() if v == 3] + sorted([k for k, v in value_counts.items() if v == 1], reverse=True))  # Three of a Kind
    elif counts == [2, 2, 1]:
        pairs = sorted([k for k, v in value_counts.items() if v == 2], reverse=True)
        kicker = [k for k, v in value_counts.items() if v == 1]
        return (3, pairs + kicker)  # Two Pair
    elif 2 in counts:
        return (2, [k for k, v in value_counts.items() if v == 2] + sorted([k for k, v in value_counts.items() if v == 1], reverse=True))  # One Pair
    else:
        return (1, values)  # High Card

def compare_hands(hand1, hand2):
    rank1, values1 = get_hand_rank(hand1)
    rank2, values2 = get_hand_rank(hand2)

    if rank1 > rank2:
        return 1  # Player 1 wins
    elif rank1 < rank2:
        return 2  # Player 2 wins
    else:
        return 1 if values1 > values2 else 2

def count_player1_wins(hands):
    for hand in hands:
        player1 = hand[:5]
        player2 = hand[5:]
        if compare_hands(player1, player2) == 1:
            print("Player 1")
        else:
            print("Player 2")
    return 

n = int(input().strip())
hands = [input().strip().split() for _ in range(n)]

count_player1_wins(hands)
