from models.card import Card, Suit
from itertools import combinations, permutations, product


def card_print(cards: list[Card]):
    return " ".join(map(str, cards))

def card_combination(cards:list[Card], n: int):
    return list(map(list,combinations(cards, n)))

def card_set_combination(cards_set1: list[Card], cards_set2: list[Card]):
    res = []
    for m_set in product(cards_set1, cards_set2):
        temp_res = list(m_set[0])
        temp_res.extend(list(m_set[1]))
        res.append(temp_res)
    return res
    # return product(cards_set1, cards_set2)