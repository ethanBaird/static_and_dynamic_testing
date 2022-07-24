import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card('hearts', 1)
        self.card2 = Card('clubs', 7)
        self.cards = [self.card1, self.card2]

    def test_can_check_for_ace__card_is_ace(self):
        is_ace = CardGame.check_for_ace(self.card1)
        self.assertEqual(True, is_ace)

    def test_can_check_for_ace__card_not_ace(self):
        is_ace = CardGame.check_for_ace(self.card2)
        self.assertEqual(False, is_ace)

    def test_highest_card__card_1_highest(self):
        highest = CardGame.highest_card(self.card2, self.card1)
        self.assertEqual(self.card2, highest)

    def test_highest_card__card_2_highest(self):
        highest = CardGame.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, highest)

    def test_highest_card__cards_equal(self):
        highest = CardGame.highest_card(self.card1, self.card1)
        self.assertEqual('These cards have the same value!', highest)

    def test_cards_total(self):
        total = CardGame.card_total(self.cards)
        self.assertEqual(8, total)

    