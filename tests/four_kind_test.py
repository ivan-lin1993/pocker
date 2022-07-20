import unittest
from models.card import Card, Suit
from Card.pocker_hand import PockerHand

class TestFourKind(unittest.TestCase):

    def test1(self):
        res = PockerHand.four_kind([
            Card(1, Suit.Spade),
            Card(1, Suit.Heart),
            Card(1, Suit.Club),
            Card(1, Suit.Diamond)
        ])
        self.assertEqual(set(res[0]), set([
            Card(1, Suit.Spade),
            Card(1, Suit.Heart),
            Card(1, Suit.Club),
            Card(1, Suit.Diamond)]))
    

    def test2(self):
        res = PockerHand.four_kind([
            Card(1, Suit.Spade),
            Card(1, Suit.Heart),
            Card(1, Suit.Club),
            Card(2, Suit.Club),
            Card(2, Suit.Spade),
            Card(2, Suit.Heart),
            Card(2, Suit.Diamond),
            Card(1, Suit.Diamond),
        ])
        
        self.assertEqual(set(res[0]), set([
            Card(1, Suit.Spade),
            Card(1, Suit.Heart),
            Card(1, Suit.Club),
            Card(1, Suit.Diamond)] ))
        self.assertEqual(set(res[1]), set([
            Card(2, Suit.Spade),
            Card(2, Suit.Heart),
            Card(2, Suit.Club),
            Card(2, Suit.Diamond)]))

