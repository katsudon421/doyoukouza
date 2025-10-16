import random

sum = 0
for q in range(100000):
    deck = []
    for i in range(13):
        deck.append(1)
    for i in range(4):
        deck.append(2)
    for i in range(9):
        deck.append(3)
    deck.append(4)
    for i in range(2):
        deck.append(5)
    for i in range(2):
        deck.append(6)
    for i in range(29):
        deck.append(0)
    hand = []
    random.shuffle(deck)
    while deck[0] != 1 and deck[1] != 1 and deck[2] != 1 and deck[3] != 1 and deck[4] != 1 and deck[5] != 1 and deck[6] != 1:
        random.shuffle(deck)
    for i in range(8):
        hand.append(deck[i])
    arven = 0
    energy = 0
    secret = 0
    buddy = 0
    evo = 0
    for card in hand:
        if card == 2:
            arven += 1
        elif card == 3:
            energy += 1
        elif card == 4:
            secret += 1
        elif card == 5:
            buddy += 1
        elif card == 6:
            evo += 1
    if secret >= 1:
        sum += 1
    elif arven >= 1 and energy >= 1:
        sum += 1
    elif buddy >= 1 and evo >= 1 and energy >= 1:
        sum += 1

print(sum)
