from models.card import Card
from enum import Enum

class SortType(Enum):
    NUMBER = 0
    SUIT = 1

class CardSortedStrategy:
    def __init__(self) -> None:
        pass

    def sort(self, cards: list[Card]) -> list[Card]:
        NotImplementedError


class CardSortedGeneral(CardSortedStrategy):
    def __init__(self, sort_type: SortType = SortType.NUMBER) -> None:
        super().__init__()
        self._sort_type = sort_type
    
    def sort(self, cards: list[Card]) -> list[Card]:
        if self._sort_type == SortType.SUIT:
            return sorted(cards, key=lambda x:(x.suit.value[0], x.number))
        elif self._sort_type == SortType.NUMBER:
            return sorted(cards, key=lambda x:(x.number, x.suit.value[0]))
        else:
            return cards