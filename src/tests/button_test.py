import unittest
from ui.button import Button


class TestButton(unittest.TestCase):
    def setUp(self):
        self.button = Button(10, 100, False)

    def test_button_exists_after_creation(self):
        self.assertNotEqual(self.button, None)
