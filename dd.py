from models.card import Card, Suit
from utils.utils import card_print
from models.card import Card, Suit
from Card.pocker_hand import PockerHand


# cards = [
#     Card(1, Suit.Spade),
#     Card(1, Suit.Heart),
#     Card(1, Suit.Club),
#     Card(1, Suit.Diamond),
#     Card(2, Suit.Spade),
#     Card(2, Suit.Heart),
#     Card(2, Suit.Club),
#     Card(2, Suit.Diamond),
# ]

# a = PockerHand.full_house(cards)
# print(a)


cards = [
    Card(1, Suit.Spade),
    Card(2, Suit.Spade),
    Card(3, Suit.Spade),
    Card(4, Suit.Spade),
    Card(5, Suit.Spade),
    Card(6, Suit.Spade),
    Card(1, Suit.Heart),
    Card(2, Suit.Heart),
    Card(3, Suit.Heart),
    Card(4, Suit.Heart),
    Card(5, Suit.Heart),
    Card(6, Suit.Heart),
    Card(1, Suit.Club),
    Card(2, Suit.Club),
    Card(3, Suit.Club),
    Card(4, Suit.Club),
    Card(5, Suit.Club),
    Card(6, Suit.Club),
    Card(1, Suit.Club),
    Card(2, Suit.Club),
    Card(3, Suit.Club),
    Card(4, Suit.Club),
    Card(5, Suit.Club),
    Card(6, Suit.Club),
]

print("====")
print(PockerHand.four_kind(cards))
