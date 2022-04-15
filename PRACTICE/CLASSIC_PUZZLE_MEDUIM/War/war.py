# init cards
# save cards values in dict
# {'2D': 0, '2H': 0, ..., 'AC': 12, 'AS': 12}
cards_suits = ['D', 'H', 'C', 'S']
cards_order = ['2', '3', '4', '5',
               '6', '7', '8', '9',
               '10', 'J', 'Q', 'K',
               'A']
cards_comb = [(f'{value}{suit}', index)
              for index, value in enumerate(cards_order) for suit in cards_suits]
cards = dict(cards_comb)

# clean memory
del cards_suits
del cards_order
del cards_comb

# init players cards
# players decks of cards
p1 = list()
p2 = list()
# players cards for each turn
p1bet = list()
p2bet = list()

# read inputs
n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    p1.append(cardp_1)
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    p2.append(cardp_2)


# return the number of winner player or None if the cards are equals
def fight(p1card, p2card):
    if (cards[p1card] > cards[p2card]): return 1
    elif (cards[p1card] < cards[p2card]): return 2
    return None


turns = 0
while True:
    p1Card = p1.pop(0)
    p2Card = p2.pop(0)
    p1bet.append(p1Card)
    p2bet.append(p2Card)
    winner = fight(p1Card, p2Card)
    # war
    if not winner:
        # a player runs out of cards during a "war"
        if len(p1) < 3 or len(p2) < 3:
            print('PAT')
            break
        # take 3 cards from each player
        p1bet.extend(p1[0:3])
        p2bet.extend(p2[0:3])
        del p1[0:3]
        del p2[0:3]
    else:
        if winner == 1: p1.extend(p1bet + p2bet)
        if winner == 2: p2.extend(p1bet + p2bet)
        p1bet.clear()
        p2bet.clear()
        turns += 1
        
        # checking if the game is ended
        if len(p1) == 0:
            print(f'2 {turns}')
            break
        if len(p2) == 0:
            print(f'1 {turns}')
            break