from ctypes import util
from models.card import Card
from Card.card_sort_handler import CardSortedGeneral, SortType
from utils.utils import card_combination, card_set_combination
from itertools import combinations, permutations, product

class PockerHand:

    @staticmethod
    def count_of_cards(cards: list[Card]) -> dict[int, list[Card]]:
        ccount: dict[int, list[Card]] = {}
        for c in cards:
            if c.number not in ccount:
                ccount[c.number] = [c]
            else:
                ccount[c.number].append(c)
        return ccount

    @staticmethod
    def get_same_num(count_cards: dict[int, list[Card]], count: int) -> list[list[Card]]:
        res = []
        for _, _cards_i in count_cards.items():
            if len(_cards_i) >= count:
                res.extend(card_combination(_cards_i, count))
        return res

    # Straight flush 同花順
    @staticmethod
    def straight_flush(cards: list[Card]) -> list[list[Card]]:
        if len(cards) < 5:
            return ([[]], cards) 
        ccount = {}
        for c in cards:
            if c.suit not in ccount:
                ccount[c.suit] = {c}
            else:
                ccount[c.suit].add(c)
        
        res = []
        for _, _cards_i in ccount.items():
            if len(_cards_i) >= 5:
                for _card_set in card_combination(_cards_i, 5):
                    # NotImplemented
                    pass
                
        return res

    
    # Four of a kind 鐵支
    @staticmethod
    def four_kind(cards: list[Card]) -> list[list[Card]]:
        if len(cards) < 4:
            return ([[]], cards) 
        res = []
        ccount = PockerHand.count_of_cards(cards)
        res.extend(PockerHand.get_same_num(ccount, 4))
        return res
        
    # Full house 葫蘆
    @staticmethod
    def full_house(cards: list[Card]) -> list[list[Card]]:
        if len(cards) < 5:
            return ([[]], cards) 
        
        res = []
        three_kind = PockerHand.three_kind(cards)
        pair = PockerHand.pair(cards)
        for t in three_kind:
            for p in pair:
                if t[0].number == p[0].number:
                    continue
                res.extend(card_set_combination([t], [p]))
        return res

    # Flush 同花
    @staticmethod 
    def flush(cards: list[Card]) -> list[list[Card]]:
        if len(cards) < 5:
            return ([[]], cards) 
        ccount = {}
        for c in cards:
            if c.suit not in ccount:
                ccount[c.suit] = [c]
            else:
                ccount[c.suit].append(c)
        
        res = []
        for _, _cards_i in ccount.items():
            if len(_cards_i) >= 5:
                res.extend(card_combination(_cards_i, 5))
                
        return res

    # Straight 順子
    @staticmethod
    def straight(cards: list[Card]) -> list[list[Card]]:
        pass
    # Three of a kind 三條
    @staticmethod 
    def three_kind(cards: list[Card]) -> list[list[Card]]:
        res = []
        ccount = PockerHand.count_of_cards(cards)
        res.extend(PockerHand.get_same_num(ccount, 3))
        return res
    # Two pair
    @staticmethod
    def two_pair(cards: list[Card]) -> list[list[Card]]:
        res = []
        pair_list = PockerHand.pair(cards)
        print(pair_list)
        for i_pair in pair_list:
            for j_pair in pair_list:
                if i_pair[0].number==j_pair[0].number:
                    continue
                res.extend(card_set_combination([i_pair], [j_pair]))
        return res
        
    # One pair
    @staticmethod
    def pair(cards: list[Card]) -> list[list[Card]]:
        res = []
        ccount = PockerHand.count_of_cards(cards)
        res.extend(PockerHand.get_same_num(ccount, 2))
        return res
