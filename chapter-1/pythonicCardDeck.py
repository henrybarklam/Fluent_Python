import collections
from random import choice

Card = collections.namedtuple("Card", ['rank', 'suit'])


'''
You want to use the same names for the special methods in your class as those used in the standard library
because it allows the user to use your code without needing a special understanding of how it was written
but also allows you to use standard functions as they'll call standard library special functions on your 
class

'''
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks ]

    def __len__(self):
        print("Using this one")
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    

def main():
    beer_card = Card('7', 'spades')
    print(beer_card)
    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print(choice(deck))
    print("Automatically supports splicing:")
    print(deck[12::13])

main()