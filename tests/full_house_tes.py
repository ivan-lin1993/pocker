import unittest
from models.card import Card, Suit
from Card.pocker_hand import PockerHand

class TestFullHouseKind(unittest.TestCase):

    def test1(self):
        res = PockerHand.full_house([
            Card(1, Suit.Spade),
            Card(1, Suit.Heart),
            Card(1, Suit.Club),
            Card(2, Suit.Spade),
            Card(2, Suit.Heart),
            Card(2, Suit.Club),
            Card(3, Suit.Spade),
            Card(3, Suit.Heart),
            Card(3, Suit.Club),
        ])
        ans = [[Card(1, Suit.Spade),
            Card(1, Suit.Heart),
            Card(1, Suit.Club),
            Card(2, Suit.Spade),
            Card(2, Suit.Heart),]]
        self.assertCountEqual()
        self.assertSequenceEqual()
    

    # def test2(self):
    #     res = PockerHand.four_kind([
    #         Card(1, Suit.Spade),
    #         Card(1, Suit.Heart),
    #         Card(1, Suit.Club),
    #         Card(2, Suit.Club),
    #         Card(2, Suit.Spade),
    #         Card(2, Suit.Heart),
    #         Card(2, Suit.Diamond),
    #         Card(1, Suit.Diamond),
    #     ])
        
    #     self.assertEqual(set(res[0]), set([
    #         Card(1, Suit.Spade),
    #         Card(1, Suit.Heart),
    #         Card(1, Suit.Club),
    #         Card(1, Suit.Diamond)] ))
    #     self.assertEqual(set(res[1]), set([
    #         Card(2, Suit.Spade),
    #         Card(2, Suit.Heart),
    #         Card(2, Suit.Club),
    #         Card(2, Suit.Diamond)]))

