from enum import Enum
from dataclasses import dataclass


class Suit(Enum):
    Spade = (0,'♠')
    Heart = (1,'♥')
    Diamond = (2,'♦')
    Club = (3,'♣')

@dataclass(frozen=True, order=True)
class Card:
    number: int
    suit: Suit

    def __str__(self):
        if self.number == 1:
            s_number = 'A'
        elif self.number == 11:
            s_number = 'J'
        elif self.number == 12:
            s_number = 'Q'
        elif self.number == 13:
            s_number = 'K'
        else:
            s_number = str(self.number)
            
        return f"{str(self.suit.value[1])}{s_number}"

    def __repr__(self):
        return str(self)