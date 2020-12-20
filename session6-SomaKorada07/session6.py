vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

suits = ['spades', 'clubs', 'hearts', 'diamonds']

def lambda_deck():
    """
    Single expression to prepare 52 cards in a deck
    Inputs: No input
    Output: Returns all cards in a deck
    """
    return list(map(lambda x:x, zip(vals * len(suits), suits * len(vals))))

def prepare_deck(vals= vals, suits = suits):
    """
    Prepares 52 cards in a deck using the vals and suits
    Inputs: Takes vals and suits as inputs
    Output: Returns all cards in a deck
    """
    deck = []

    for _, i in enumerate(vals):
        for _, j in enumerate(suits):
            deck.append((i,j))

    return deck


def change_vals(vals):
    """
    Changing vals to have all numeric values
    Input: Takes vals as input which could be player's card values or all cards in the deck
    """
    for n, i in enumerate(vals):
        if i == "jack":
            vals[n] = '11'
        elif i == "queen":
            vals[n] = '12'
        elif i == "king":
            vals[n] = '13'
        elif i == "ace":
            vals[n] = '14'


def determine_rank(player_set: 'cards of the player', vals = vals) -> 'rank of the player':
    """
    Determines rank of the player based on the cards in the set
    Input: Takes player's cards as input
    Output: Returns player's rank
    """
    player_set_suits = set()
    player_set_vals = []
    player_set_max = 0
    player_set_rank = 100
    count_one = 0
    count_two = 0
    flag = False

    for card in player_set:
        player_set_vals.append(card[0])
        player_set_suits.add(card[1])

    change_vals(player_set_vals)

    if len(player_set_suits) == 1:
        player_set_rank = 5

        for i in player_set_vals:
            if i in vals[-5:]:
                count_one += 1
                if i == '10':
                    flag = True
            elif i in vals[4:9]:
                count_two += 1

        if count_one == len(player_set_vals):
            player_set_rank = 1
        elif count_two == len(player_set_vals) - 1 and flag:
            player_set_rank = 2

    else:
        player_set_counter = {i : player_set_vals.count(i) for i in player_set_vals}

        counts = player_set_counter.values()

        if int(sorted(counts, reverse=True)[0]) == len(player_set) - 1:
            player_set_rank = 3
        elif int(sorted(counts, reverse=True)[0]) == len(player_set) - 2:
            if len(player_set) != 3:
                if int(sorted(counts, reverse=True)[0]) + int(sorted(counts, reverse=True)[1]) == len(player_set):
                    player_set_rank = 4
                else:
                    player_set_rank = 7
            else:
                for i in (0, len(player_set_vals) - 2):
                    if int(sorted(player_set_vals, reverse=True)[i]) - int(sorted(player_set_vals, reverse=True)[i + 1]) == 1:
                        player_set_rank = 6
                    elif int(sorted(player_set_vals, reverse=True)[i]) - int(sorted(player_set_vals, reverse=True)[i + 1]) == 0:
                        player_set_rank = 7
                    else:
                        player_set_rank = 10
        elif sorted(counts, reverse=True)[0] == len(player_set) - 3:
            if len(player_set) == 5:
                if int(sorted(counts, reverse=True)[0]) + int(sorted(counts, reverse=True)[1]) + int(sorted(counts, reverse=True)[2]) == len(player_set):
                    player_set_rank = 8
                else:
                    player_set_rank = 9
            elif len(player_set) == 4:
                if int(sorted(counts, reverse=True)[0]) + int(sorted(counts, reverse=True)[1]) == len(player_set):
                    player_set_rank = 8
                if int(sorted(counts, reverse=True)[0]) + int(sorted(counts, reverse=True)[1]) + int(sorted(counts, reverse=True)[2]) == len(player_set):
                    player_set_rank = 9
                else:
                    for i in (0, len(player_set_vals) - 2):
                        if int(sorted(player_set_vals, reverse=True)[i]) - int(sorted(player_set_vals, reverse=True)[i + 1]) == 1:
                            player_set_rank = 6
                        elif int(sorted(player_set_vals, reverse=True)[i]) - int(sorted(player_set_vals, reverse=True)[i + 1]) == 0:
                            player_set_rank = 7
                        else:
                            player_set_rank = 10
        else:
            for i in (0, len(player_set_vals) - 2):
                if int(sorted(player_set_vals, reverse=True)[i]) - int(sorted(player_set_vals, reverse=True)[i + 1]) == 1:
                    player_set_rank = 6
                elif int(sorted(player_set_vals, reverse=True)[i]) - int(sorted(player_set_vals, reverse=True)[i + 1]) == 0:
                    player_set_rank = 7
                else:
                    player_set_rank = 10            

    return player_set_rank


def determine_winner(set1: 'cards of player 1', set2: 'cards of player 2') -> 'winner between player 1 and player 2':
    """
    Determines winner based on the rules of the game
    Inputs: Cards of 2 players
    Output: Winner between the 2 players
    """
    set1_vals = []
    set2_vals = []
    set1_position = None
    set2_position = None

    if (len(set1) >= 0 and len(set1) < 3) or (len(set2) >= 0 and len(set2) < 3):
        raise ValueError('Player should have at least 3 cards!')

    if len(set1) != len(set2):
        raise ValueError('Each player does not have equal number of cards!')

    combined_set = set1 | set2

    if len(combined_set) != (len(set1) + len(set2)):
        raise ValueError('Two players cannot have same card!')

    for card in set1:
        set1_vals.append(card[0])

    for card in set2:
        set2_vals.append(card[0])

    change_vals(vals)

    change_vals(set1_vals)

    change_vals(set2_vals)

    set1_rank = determine_rank(set1, vals)
    set1_highest = sorted(set1_vals, reverse=True, key = lambda x: int(x))[0]

    set2_rank = determine_rank(set2, vals)
    set2_highest = sorted(set2_vals, reverse=True, key = lambda x: int(x))[0]

    for n, i in enumerate(vals):
        if i == set1_highest:
            set1_position = n
        if i == set2_highest:
            set2_position = n

    if set1_rank < set2_rank:
        winner = "player1"
    elif set1_rank == set2_rank:
        if set1_position > set2_position:
            winner = "player1"
        elif set1_position == set2_position:
            winner = "draw"
        else:
            winner = "player2"
    else:
        winner = "player2"

    return winner