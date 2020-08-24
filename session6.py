import random

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
vals_dict = {'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}


def create_cards_lambda(vals, suits):
    """creates a deck of cards
    Inputs:
        vals: list of values available for cards
        suits: list of suits available for cards
    returns:
        Deck of cards
    """
    return list(map(lambda x :x,zip(vals*len(suits),suits*len(vals))))

def create_cards(vals,suits):
    """creates a deck of cards
    Inputs:
        vals: list of values available for cards
        suits: list of suits available for cards
    returns:
        Deck of cards    
    """
    
    deck = [(value, suite) for value in vals for suite in suits]
    #print(deck)
    return deck

def cards_eval(cards_set):
    """Evaluates the set of cards
    Inputs:
        cards_set: list of cards to be evaluated

    returns:
        Rank of set of cards    
    """
    values = sorted([v[0] for v in cards_set])
    suits = [v[1] for v in cards_set]
    straight = (values == range(min(values), max(values)+1))
    flush = all(s == suits[0] for s in suits)

    if straight and flush:
        if values[0] == 10:
            return 9, None
        else: return 8, max(values)

    pairs = []
    pair_present = False
    three_of_a_kind = False
    three_value = None
    for v in set(values):
        if values.count(v) == 4:
            return 7, v
        if values.count(v) == 3:
            three_of_a_kind = True
            three_value = v
        if values.count(v) == 2:
            pair_present = True
            pairs.append(v)

    if three_of_a_kind and pair_present: return 6, (three_value, pairs[0])
    if flush: return 5, None
    if straight: return 4, max(values)
    if three_of_a_kind: return 3, three_value
    if len(pairs) == 2: return 2, pairs
    if len(pairs) == 1: return 1, pairs[0]
    return 0, max(values)

def cards_conversion(cards):
    """Evaluates the set of cards
    Inputs:
        cards_set: list of cards to be evaluated

    returns:
        Rank of set of cards    
    """
    converted_cards = []
    for i in cards:
        try:
            value = int(i[0])
        except:
            value = vals_dict[i[0]]
        converted_cards.append((value, i[1]))
    return converted_cards

            
def poker(cards : "List of cards" = create_cards(vals,suits),set : "List of number of cards" = [3,4,5],player1 : "List of player1 cards" = [],player2 : "List of player 2 cards" = []):
    """Declares the winner among 2 players
    Inputs:
        cards: Deck of cards
        set: number of cards for each player
        player1: list of cards for player 1
        player2: list of cards for player2
        
    """
    for i in range(random.choice(set)):
        player1.append(random.choice(cards))
        player2.append(random.choice(cards))
    player1_cards = cards_conversion(player1)
    player2_cards = cards_conversion(player2)
    print(player1)
    print(player2)
    print(player1_cards)
    print(player2_cards)
    player1_rank, player1_max_value = cards_eval(player1_cards)
    player2_rank, player2_max_value = cards_eval(player2_cards)
    print(player1_rank)
    print(player2_rank)
    
    if player1_rank > player2_rank:
        print("Player1 wins")
    elif player2_rank > player1_rank:
        print("player2 wins")
    elif((player1_rank == player2_rank) and player1_rank != 0):
        if(player1_max_value > player2_max_value):
            print("player1 wins")
        else: print ("player2 wins")
    else: print("No one Win")
    
poker()


#create_cards(vals,suits)
#final[5]