from game.game import Game
from models.player import Player
from Card.card_sort_handler import CardSortedGeneral, SortType

g1, g2 = CardSortedGeneral(SortType.SUIT), CardSortedGeneral(SortType.NUMBER)

p1 = Player('Ivan', g1)
p2 = Player('Jesse', g1)
p3 = Player('Sunny', g2)
p4 = Player('Amy', g2)

players = [p1, p2, p3, p4]

g = Game(players)

g.deal()
g.show_status()

g.over()
g.show_status()

g.deal()
g.show_status()
