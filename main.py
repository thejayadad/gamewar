
from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

mycards = [(s,r) for s in SUITE for r in RANKS]

for r in RANKS:
    for s in SUITE:
        mycards.append((s,r))

class Deck:
    def __init__ (self):
        print("New Deck")
        self.allcards =



class Hand:
    pass
