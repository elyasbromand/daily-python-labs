import random

cards = ["Jack", "Queen", "King"]

random.shuffle(cards)

# it changes the cards array itself
for card in cards:
    print(card)

