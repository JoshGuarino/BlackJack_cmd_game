#class constrcutor for players
class Player: 
    def __init__(self, name):
        self.name = name
        self.money = 200
        self.hand = []
        self.hand_count = 0  
        self.hand_index = -1  
    def hit(self, deck_):
        self.hand_index += 1
        self.hand.append(deck_.current_deck.pop())
        current_card_name = self.hand[self.hand_index]
        self.hand_count += self.hand[self.hand_index].card_value
        if self.hand_count > 21:
            for x in self.hand:
                if x.card_name == 'ace':
                    x.card_value = 1
                    self.hand_count -= 10