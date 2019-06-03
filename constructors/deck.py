import random

#class constructor for cards
class Card:
    def __init__(self, suit, card_name, card_value):
        self.suit = suit
        self.card_name = card_name
        self.card_value = card_value

#class constructor for the deck
class Deck:
    def __init__(self):
        self.current_deck = []
        self.suits = ['hearts', 'diamonds','spades','clubs']
        self.cards = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
    def initialize(self):
        for i in range(len(self.suits)):
            for j in range(len(self.cards)):
                if (self.cards[j]=='2' or self.cards[j]=='3' or self.cards[j]=='4' or self.cards[j]=='5' or self.cards[j]=='6' or self.cards[j]=='7' or self.cards[j]=='8' or self.cards[j]=='9'):
                    self.current_deck.append(Card(self.suits[i], self.cards[j], int(self.cards[j])))
                elif (self.cards[j]=='10' or self.cards[j]=='jack' or self.cards[j]=='queen' or self.cards[j]=='king'):   
                    self.current_deck.append(Card(self.suits[i], self.cards[j], 10))
                else:
                    self.current_deck.append(Card(self.suits[i], self.cards[j], 11))
    def shuffle(self):
        for card in self.current_deck:
            j = random.randrange(0, len(self.current_deck))
            temp = card
            card = self.current_deck[j]
            self.current_deck[j] = temp