from typing import List
from models.card import Card, Suit
import random
from models.player import Player

class Game:
    def __init__(self, players: List[Player]):
        self._players = players
        self._player_number = len(players)
        self._init_deck()            


    def _init_deck(self):
        self._deck = []
        numbers = list(range(1,14))
        for s in Suit:
            for n in numbers:
                self._deck.append(Card(n, s))

    def deal(self):
        random.shuffle(self._deck)
        for i,card in enumerate(self._deck):
            self._players[i % self.player_number].get_card(card)

    def over(self):
        for p in self._players:
            p.empty_hand()

    def show_status(self):
        for p in self._players:
            print(p)

    @property
    def player_number(self):
        return self._player_number


    