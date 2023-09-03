from const import MAX_POINT

class Player:
    def __init__(self, cards):
        self.cards = [cards[0], cards[1]]
        self.total_point = cards[0] + cards[1]

    def draw(self, card):
        def check_is_ace():
            return True if card == 11 else False
        
        def get_ace_value():
            if (self.total_point + card <= MAX_POINT):
                return 11
            
            elif (self.total_point + 10 <= MAX_POINT):
                return 10
            
            return 1
        
        is_ace = check_is_ace()

        self.total_point += get_ace_value() if is_ace else card
        self.cards.append(card)
        return card
    
    def show_current_hand(self):
        return self.cards
    
    def get_total_points(self):
        return self.total_point
