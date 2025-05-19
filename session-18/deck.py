import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit
    

class FrenchDeck:
    def __init__(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

    def __setitem__(self, position, value):
        if isinstance(value, Card):
            self.cards[position] = value
        else:
            print("Only Card objects can be assigned to the deck.")
            
    def shuffle(self):
        random.shuffle(self.cards)


deck = FrenchDeck()

print("Random card:", random.choice(deck))
print("First card:", deck[0])

print("\nAll cards in the deck:")
for card in deck:
    print(card)

print("\nShuffling deck...")
random.shuffle(deck)
print("Top card after shuffle:", deck[0])