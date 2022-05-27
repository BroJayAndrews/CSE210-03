import random

class Card:
    def __init__(self):
        self.score = 0
        self.card1 = 0
        self.card2 = 0
    def firstcardflip():
        Card.card1 = random.randint(1,13)
        return Card.card1
    def secondcardflip(card,hilo):
        Card.card2 = random.randint(1,13)
        print(f'The Second Card Is {Card.card2}')
        if card < Card.card2 and hilo == "high":
            Card.score = 100
        elif card > Card.card2 and hilo =="low":
            Card.score = 100
        elif card == Card.card2:
            Card.score = 0
            print(f'The Score is 0 Points The Card is the same card')
        else:
            Card.score = -75
        return Card.score

