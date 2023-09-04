import random

class Dealer:
    def __init__(self):
        # 10 * 2 since 3 type J Q K
        self.deck = list(range(1,12)) * 4 + [10] * 2
        random.shuffle(self.deck)
    
    def deal(self):
        cards = []
        cards.append(self.deck.pop())
        cards.append(self.deck.pop())
        return cards
    
    def draw(self):
        return self.deck.pop()