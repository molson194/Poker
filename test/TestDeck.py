import os
import unittest
import sys

sys.path.insert(0, os.path.abspath( os.path.join(os.path.dirname(__file__), '../src/') ))
from Deck import Deck

class TestDeck(unittest.TestCase):

    def test_deck_length(self):
        deck = Deck()
        self.assertEqual(len(deck.Cards), 52, "52 cards in a deck")

if __name__ == '__main__':
    unittest.main()