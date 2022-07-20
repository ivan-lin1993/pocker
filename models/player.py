from models.card import Card
from Card.card_sort_handler import CardSortedStrategy

class Player:
    def __init__(self, name, order_engine: CardSortedStrategy):
        self._name = name
        self._hands: list[Card] = []
        self._order_engine = order_engine
    
    def get_card(self, c: Card):
        self._hands.append(c)

    def empty_hand(self):
        self._hands = []
    
    def show_cards(self):
        res = ""
        _hand = self._order_engine.sort(self._hands)
        for c in _hand:
            res += f"{str(c)} "

        return res
    
    def __str__(self) -> str:
        return f"""{self._name} hold cards: {len(self._hands)}
------------------------------------------------
{self.show_cards()}\n"""