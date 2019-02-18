#class constrcutor for dealer
class dealer:
    def __init__(self):
        self.money = 10000
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
    def deal(self, deck_, player_):
        for i in range (2):
            self.hand_index += 1
            self.hand.append(deck_.current_deck.pop())
            current_card_name = self.hand[i]
            self.hand_count += self.hand[i].card_value
        for i in range (2):
            player_.hand_index += 1
            player_.hand.append(deck_.current_deck.pop())
            current_card_name = player_.hand[i]
            player_.hand_count += player_.hand[i].card_value    
    def strategy(self, deck_):
        while self.hand_count < 17:
            self.hit(deck_)
            if self.hand_count > 21:
                for x in self.hand:
                    if x.card_name == 'ace':
                        x.card_value = 1
                        self.hand_count -= 10
    def reset_table(self, deck_, player_):
        #reset dealer
        for x in range(self.hand_index + 1):
            if self.hand[x].card_name == 'ace':
                self.hand[x].card_value = 11
        for x in range(self.hand_index + 1):
            deck_.current_deck.append(self.hand.pop())
        self.hand_count = 0
        self.hand_index = -1

        #reset player
        for x in range(player_.hand_index + 1):
            if player_.hand[x].card_name == 'ace':
                player_.hand[x].card_value = 11
        for x in range(player_.hand_index + 1):
            deck_.current_deck.append(player_.hand.pop(0))        
        player_.hand_count = 0
        player_.hand_index = -1