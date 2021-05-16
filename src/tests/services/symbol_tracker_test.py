import unittest
from services.symbol_tracker import SymbolTracker


class TestSymbolTracker(unittest.TestCase):
    def setUp(self):
        self.st = SymbolTracker()

    def test_correct_classification_reduces_the_nbr_of_remaining_symbols(self):
        original_value = self.st.get_nbr_of_remaining_symbols()
        self.st.correctly_classified('src/assets/symbol_images/affricate0.png')
        new_value = self.st.get_nbr_of_remaining_symbols()
        self.assertNotEqual(new_value, original_value)
